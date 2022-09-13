from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    dsc = db.Column(db.String(500))
    press = db.Column(db.Date())
    posted_date = db.Column(db.DateTime(), nullable=False)
    link = db.Column(db.String(200))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Barcode_categories(db.Model):
    b_category_id = db.Column(db.Integer, primary_key=True)
    b_category_name = db.Column(db.String(200))

class Recipe_ingredient(db.Model):
    __tablename__ = 'recipe_ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'),nullable=False)
    ingredient_id = db.Column(db.Integer,db.ForeignKey('recipes.recipe_id'))

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    ingredient_name = db.Column(db.String(200))

class Fridge(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    product = db.Column(db.String(200))
    barcode = db.Column(db.String(500),nullable=True)
    user = db.relationship('User', backref=db.backref('fidge_set'))
    subclass = db.Column(db.String(150), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    exp_date = db.Column(db.Date, nullable=False)
    adding_date = db.Column(db.DateTime(), nullable=True)
    modify_date = db.Column(db.DateTime(), nullable=True)
    remain_date = db.Column(db.DateTime(),nullable=True)

class Barcode_companies(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(500))

class Barcode(db.Model):
    barcode_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.String(500), nullable=True)
    b_category_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    product_name = db.Column(db.String(500))
    shelf_life = db.Column(db.Integer)
    exp_days = db.Column(db.Integer)


class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_name = db.Column(db.String(500), nullable=False)
    recipe_desc = db.Column(db.String(500), nullable=False)
    views = db.Column(db.Integer)
    recommand = db.Column(db.Integer)
    scrap = db.Column(db.Integer)
    cooking_serving = db.Column(db.Integer)
    level = db.Column(db.Integer)
    cooking_time = db.Column(db.Integer)

class Recipe_situation(db.Model):
    situation_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer)

class Situation(db.Model):
    situation_id = db.Column(db.Integer, primary_key=True)
    situation_name = db.Column(db.String(200))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

    