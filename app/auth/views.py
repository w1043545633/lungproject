from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			if user.role.name == "Doctor":
				return redirect(request.args.get('next') or url_for('main.index'))
			elif user.role.name == "Upload_data":
				return redirect(request.args.get('next') or url_for('main.upload_data'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)



@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logout.')
	return redirect(url_for('auth.login'))
