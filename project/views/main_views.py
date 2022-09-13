from flask import Blueprint, url_for,render_template
from werkzeug.utils import redirect

bp = Blueprint('main',__name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo ~.~'


@bp.route('/', methods=['POST','GET'])
def index():
    return render_template('cp_main.html')

@bp.route('/main/')
def main():
    return redirect(url_for('fridge._list'))

@bp.route('/statistics/')
def statistics():
    return render_template('fridge/cp_statistics.html')