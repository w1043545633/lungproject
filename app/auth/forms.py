#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class LoginForm(Form):
	email = StringField('账号', validators=[Required(), Length(1, 64), Email()],
						render_kw={"placeholder": "your email"})
	password = PasswordField('密码', validators=[Required()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登录', render_kw={"style": "width: 75px; margin-left:125px; color: #23527c;"})