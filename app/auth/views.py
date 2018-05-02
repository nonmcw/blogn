from flask import render_template, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.date).first()
        if user is not None and User.verify_password(form.password.date):
            login_user(user, form.remember_me.date)
            redirect(request.args.get('next') or url_for('main.index'))
        flash('invalid username or password')
    return render_template('auth/login.html', form=form)
