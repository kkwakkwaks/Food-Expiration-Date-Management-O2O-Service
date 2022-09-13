from datetime import datetime
from urllib.response import addinfo

from flask import Blueprint, render_template, request, url_for, g, flash, Response
from werkzeug.utils import redirect

from .. import db
from ..forms import AddIngredientForm 
from ..models import Ingredient, Recipe_situation, User, Fridge, Recipes, Situation, Recipe_ingredient
from ..views.auth_views import login_required

import cv2
import pyzbar.pyzbar as pyzbar


bp = Blueprint('fridge', __name__, url_prefix='/fridge')
camera = cv2.VideoCapture(0)

@bp.route('/list/', methods=['GET','POST'])
@login_required
def _list():
    if request.method == 'GET':
        page = request.args.get('page', type=int, default=1)
        kw = request.args.get('kw', type=str, default='')
        ingredient_list = Fridge.query.filter(g.user==Fridge.user).order_by(Fridge.exp_date.asc())
        if kw:
            search = '%%{}%%'.format(kw)
            sub_query = db.session.query(Fridge.id, Fridge.product, Fridge.subclass, User.username) \
                .join(User, Fridge.user_id == User.id).subquery()
            ingredient_list = ingredient_list \
                .join(User) \
                .outerjoin(sub_query, sub_query.c.id == Fridge.id) \
                .filter(Fridge.product.ilike(search) |  # 재료
                        Fridge.subclass.ilike(search) |  # 소분류
                        User.username.ilike(search) |  # 질문작성자
                        sub_query.c.username.ilike(search)  # 답변작성자
                        ) \
                .distinct()
        ingredient_list = ingredient_list.paginate(page, per_page=10)
        return render_template('fridge/ingredient_list.html', ingredient_list=ingredient_list, page=page, kw=kw)
    return render_template('cp_main.html')
import psycopg2

def dbconn():
    host = 'jelani.db.elephantsql.com'
    user = 'gycmqpcx'
    password = 'JFjJrpR7BlY0WMoLKw8BsKSCAoFyWBcQ'
    database = 'gycmqpcx'

    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cur = conn.cursor()
    return conn, cur

@bp.route('/recipe/')
def recipe():
    conn,cur = dbconn()
    searches = None
    if request.method == 'GET':
        page = request.args.get('page', type=int, default=1)
        kw = request.args.get('kw', type=str, default='')
        recipe_list = Recipes.query.order_by(Recipes.recommand.desc())
        if kw:
            cur.execute(f"""
            select a.recipe_id, a.recipe_name, a.recipe_desc, a.views, a.recommand, a.scrap, a.cooking_serving, a.level, a.cooking_time
                ,string_agg(c.ingredient_name, ',') as ingredients
            FROM recipes a 
                join recipe_ingredient b on a.recipe_id=b.recipe_id
                join ingredient c on b.ingredient_id = c.ingredient_id
            group by a.recipe_id, a.recipe_name, a.recipe_desc, a.views, a.recommand, a.scrap, a.cooking_serving, a.level, a.cooking_time
            having 
                a.recipe_name like '%{kw}%'
                or string_agg(c.ingredient_name, ',') like '%{kw}%'
            order by 1;
            """)
            searches = cur.fetchall()
        recipe_list = recipe_list.paginate(page, per_page=10)
        conn.close()
        return render_template('fridge/cp_recipe.html', recipe_list=recipe_list, page=page, kw=kw, searches=searches)
    conn.close()
    return render_template('cp_main.html')



@bp.route('/recipe/recommend/')
def recipe_recom():
    if request.method == 'GET':
        page = request.args.get('page', type=int, default=1)
        kw = request.args.get('kw', type=str, default='')
        recipe_list = Recipes.query.order_by(Recipes.recommand.desc())
        if kw:
            search = '%%{}%%'.format(kw)
            db.session.query(Recipes, Recipe_situation, Situation, Recipe_ingredient,Ingredient)\
                .join(Recipe_ingredient, Recipes.recipe_id == Recipe_ingredient.ingredient_id)\
                .join(Ingredient, Recipe_ingredient.ingredient_id == Ingredient.ingredient_id)\
                .join(Recipe_situation, Recipes.recipe_id == Recipe_situation.recipe_id)\
                .join(Situation, Recipe_situation.situation_id == Situation.situation_id)
            recipe_list = recipe_list\
                .filter(Recipes.recipe_desc.ilike(search) |  # 재료
                        Recipes.recipe_name.ilike(search) |  # 소분류
                        Situation.situation_name.ilike(search) |  # 질문작성자
                        Ingredient.ingredient_name.ilike(search)  # 답변작성자
                        ) \
                .distinct()
        recipe_list = recipe_list.paginate(page, per_page=10)
        return render_template('fridge/cp_recipe_recom.html', recipe_list=recipe_list, page=page, kw=kw)
    return render_template('cp_main.html')


@bp.route('/detail/<int:fridge_id>/')
def detail(fridge_id):
    fridge = Fridge.query.get_or_404(fridge_id)
    return render_template('fridge/ingredient_detail.html', fridge=fridge)

@bp.route('/recipe/detail/<int:recipe_id>/')
def recipe_detail(recipe_id):
    conn,cur = dbconn()
    recipe = Recipes.query.get_or_404(recipe_id)
    cur.execute(f"""
select a.recipe_id, a.recipe_name, a.recipe_desc, e.situation_name ,a.views, a.recommand, a.scrap, a.cooking_serving, a.level, a.cooking_time
    ,string_agg(c.ingredient_name, ',') as ingredients
FROM recipes a 
    join recipe_ingredient b on a.recipe_id=b.recipe_id
    join ingredient c on b.ingredient_id = c.ingredient_id
    join recipe_situation d on a.recipe_id = d.recipe_id 
    join situation e on d.situation_id = e.situation_id 
group by a.recipe_id, a.recipe_name, e.situation_name, a.recipe_desc, a.views, a.recommand, a.scrap, a.cooking_serving, a.level, a.cooking_time
having a.recipe_id = {recipe_id};
""")
    r_detail = cur.fetchone()
    conn.close()
    return render_template('fridge/recipe_detail.html', recipe=recipe, r_detail=r_detail)


@bp.route('/add_ingredient/', methods=['GET','POST'])
@login_required
def create():
    form = AddIngredientForm()
    if request.method == 'POST' and form.validate_on_submit():
        fridge = Fridge(barcode = form.barcode.data,
                        product=form.product.data, 
                        subclass=form.subclass.data,
                        qty=form.qty.data,
                        exp_date=form.exp_date.data,
                        adding_date = form.adding_date.data,
                        user=g.user)
        db.session.add(fridge)
        db.session.commit()
        return redirect(url_for('main.main'))
    return render_template('fridge/cp_add.html', form=form)

@bp.route('/modify/<int:fridge_id>', methods=('GET','POST'))
@login_required
def modify(fridge_id):
    fridge = Fridge.query.get_or_404(fridge_id)
    if g.user != fridge.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('fridge.detail', fridge_id=fridge_id))
    if request.method == 'POST':
        form = AddIngredientForm()
        if form.validate_on_submit():
            form.populate_obj(fridge)
            fridge.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('fridge.detail', fridge_id=fridge_id))
    else:
        form = AddIngredientForm(obj=fridge)
    return render_template('fridge/cp_add.html', form=form)

@bp.route('/delete/<int:fridge_id>')
@login_required
def delete(fridge_id):
    fridge = Fridge.query.get_or_404(fridge_id)
    if g.user != fridge.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('fridge.detail', fridge_id=fridge_id))
    db.session.delete(fridge)
    db.session.commit()
    return redirect(url_for('fridge._list'))
    
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            for code in pyzbar.decode(frame):
                cv2.imwrite('barcode_image.png', frame)
                my_code = code.data.decode('utf-8')
                print("바코드 : ", my_code)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@bp.route('/video_feed/')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@bp.route('/barcode/')
def index_barcode():
    """Video streaming home page."""
    return render_template('fridge/index.html')