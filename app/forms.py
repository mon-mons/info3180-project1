from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender=SelectField('Gender', choices=[('Male','Male') , ('Female', 'Female')],validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    location= StringField('Location', validators=[DataRequired()])
    biography=TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField('Profile Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
