from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('邮箱或用户名', validators=[Required(), Length(5, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(5, 64), Email()])
    username = StringField('用户名', validators=[Required(), Length(4, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须以字母开始可包括数字和下划线')])
    password = PasswordField('密码', validators=[Required(), 
        EqualTo('password2', message='两次密码不一至')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在！')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册！')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
        EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Change Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(5, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Change Email')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email already registered.')
