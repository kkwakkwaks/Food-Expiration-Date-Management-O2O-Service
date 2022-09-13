from sqlite3 import sqlite_version_info
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields import EmailField, IntegerRangeField, SelectField,DateField,IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하슈')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하슈')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[
                            DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
                            DataRequired(), EqualTo('password2','비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일',[DataRequired(), Email()])
    gender = SelectField('성별', validators=[DataRequired('F / M')], choices=['F','M'])
    region = SelectField('지역', validators=[DataRequired('서울, 경기, 대구, 부산, 제주, 그 외')],choices=['서울','경기','대구','부산','제주','그 외'])
    age = IntegerRangeField('나이',validators=[DataRequired()])
    
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[
                            DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class AddIngredientForm(FlaskForm):
    barcode = StringField('바코드', validators=[Length(13)])
    subclass = StringField('소분류', validators=[
                            DataRequired('소분류'), Length(min=1, max=25)])
    product = StringField('제품명', validators=[DataRequired('제품명을 입력하세요')])
    qty = IntegerRangeField('수량',validators=[DataRequired('몇 개를 냉장고에 넣으시나요')])
    adding_date = DateField('냉장고 들어가는 날', validators=[DataRequired('냉장고에 재료 들어간 날짜')])
    exp_date = DateField('유통기한',validators=[DataRequired('유통기한')])
    remain_date = DateField('남은날짜')


class RecipeForm(FlaskForm):
    recipe_name = StringField('레시피이름', validators=[DataRequired(), Length(min=2, max=15)])
    recipe_desc = StringField('요리설명', validators=[DataRequired()])
    level = StringField('난이도')
    cooking_time = IntegerRangeField('요리시간', validators=[DataRequired()])