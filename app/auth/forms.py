from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email or Username', validators=[Required(), Length(5, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(5, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(4, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have...')])
    password = PasswordField('Password', validators=[Required(), 
        EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email areldy registered')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username areldy registered')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
        EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Change Password')
