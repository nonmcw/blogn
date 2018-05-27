from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length

class NameForm(FlaskForm):
    name = StringField('UserName', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    phone = StringField('phone number', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

