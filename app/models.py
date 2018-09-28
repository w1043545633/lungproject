from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	permissions = db.Column(db.Integer)
	default = db.Column(db.Boolean, default=False, index=True)
	users = db.relationship('User', backref='role', lazy="dynamic")

	@staticmethod
	def insert_roles():
		roles = {
			'Doctor': (Permission.TYPE_INFORMATION |
						 Permission.DOWNLOAD_DATA |
						 Permission.OBTAIN_RECOMMENDATION, True),
			'Upload_data': (Permission.UPLOAD_DATA, False),
			'Administrator': (0xff, False)
		}
		for r in roles:
			role = Role.query.filter_by(name=r).first()
			if role is None:
				role = Role(name=r)
			role.permissions = roles[r][0]
			role.default = roles[r][1]
			db.session.add(role)
		db.session.commit()

	def __repr__(self):
		return '<Role %r>' % self.name



class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		if self.role is None:
			if self.email == current_app.config['FLASKY_ADMIN']:
				self.role = Role.query.filter_by(permissions=0xff).first()
			if self.role is None:
				self.role = Role.query.filter_by(default=True).first()

	@property
	def password(self):
		return AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def can(self, permissions):
		return self.role is not None and \
			(self.role.permissions & permissions) == permissions

	def is_administrator(self):
		return self.can(Permission.ADMINISTER)

	def __repr__(self):
		return '<User %r>' % self.username


class Patient(db.Model):
	__tablename__ = 'patients'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	birth_date = db.Column(db.String(64))
	gender = db.Column(db.String(64))
	admission_num = db.Column(db.String(64))
	idnum = db.Column(db.String(128), unique=True)
	hospital = db.Column(db.String(64))
	cancer = db.Column(db.String(64))
	smoke = db.Column(db.String(64))
	intemperance = db.Column(db.String(64))
	take_drug = db.Column(db.String(64))
	other_bad_habits = db.Column(db.String(64))
	doctor_email = db.Column(db.String(64),index=True)
	national = db.Column(db.String(64))
	profession = db.Column(db.String(64))
	tel = db.Column(db.String(64), index=True)
	address = db.Column(db.String(64))
	f_member_tel = db.Column(db.String(64), index=True)
	family_history = db.Column(db.String(64))
	operation_history = db.Column(db.String(64))
	injured_history = db.Column(db.String(64))
	irritability_history = db.Column(db.String(64))

	diagnosis = db.Column(db.Text)
	targeted_therapy = db.Column(db.Text)
	radiotherapy = db.Column(db.Text)
	state_after_radiotherapy = db.Column(db.Text)
	drug_treatment_plan = db.Column(db.Text)
	state_after_drugtreament = db.Column(db.Text)
	clinical_stage = db.Column(db.Text)
	patient_statement = db.Column(db.Text)
	image_result = db.Column(db.Text)
	pathological_result = db.Column(db.Text)
	pathological_grade = db.Column(db.Text)
	pathological_examination_result = db.Column(db.Text)
	genetic_examination_result = db.Column(db.Text)
	tumor_marker_result = db.Column(db.Text)
	operation_time = db.Column(db.Text)
	operation_type = db.Column(db.Text)
	operation_degree = db.Column(db.Text)
	lymph_state = db.Column(db.Text)
	diagnostic_time = db.Column(db.String(64))
	dead = db.Column(db.String(64))
	death_time = db.Column(db.String(64))
	cause_of_death = db.Column(db.Text)

	sample_name = db.Column(db.String(128), index=True)
	upl_name = db.Column(db.String(64))
	pro_name = db.Column(db.String(64))
	public = db.Column(db.String(64))
	expdata_exist = db.Column(db.String(64))
	refdata_exist = db.Column(db.String(64))
	data_type = db.Column(db.String(64))
	exp_data = db.Column(db.String(128))
	ref_data = db.Column(db.String(128))

	def __repr__(self):
		return '<Patient %r>' % self.name

class AnonymousUser(AnonymousUserMixin):
	def can(self, permissions):
		return False

	def is_administrator(self):
		return False

login_manager.anonymous_user = AnonymousUser


class Permission:
	TYPE_INFORMATION = 0x01
	DOWNLOAD_DATA = 0x02
	OBTAIN_RECOMMENDATION = 0x04
	UPLOAD_DATA = 0x08
	ADMINISTER = 0x80


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))