# -*- coding: UTF-8 -*-  

from flask import render_template, request, jsonify, current_app
from . import main
from flask_login import login_required
from ..decorators import admin_required, permission_required
from ..models import Permission
from forms import PatientBaseInfoForm
from ..models import Patient
from .. import db
from werkzeug.utils import secure_filename
import os
import json



@main.route('/', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.TYPE_INFORMATION |
					Permission.DOWNLOAD_DATA |
					Permission.OBTAIN_RECOMMENDATION)
def index():
	return render_template('index.html')


@main.route('/upload_data', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.UPLOAD_DATA)
def upload_data():
	return render_template('upload_data.html')

@login_required
@permission_required(Permission.TYPE_INFORMATION |
					Permission.DOWNLOAD_DATA |
					Permission.OBTAIN_RECOMMENDATION)
@main.route('/patient_info', methods=['GET', 'POST'])
def patient_info():
	if request.form.get('name'):
		if Patient.query.filter_by(name=request.form.get('name')).first():
			patient = Patient.query.filter_by(name=request.form.get('name')).first()
		else:
			patient = Patient()
		patient.name = request.form.get('name')
		patient.birth_date = request.form.get('birth_date')
		patient.gender = request.form.get('gender')
		patient.admission_num = request.form.get('admission_num')
		patient.idnum = request.form.get('idnum')
		patient.hospital = request.form.get('hospital')
		patient.cancer = request.form.get('cancer')
		patient.smoke = request.form.get('smoke')
		patient.intemperance = request.form.get('intemperance')
		patient.take_drug = request.form.get('take_drug')
		patient.other_bad_habits = request.form.get('other_bad_habits')
		patient.doctor_email = request.form.get('doctor_email')
		patient.national = request.form.get('national')
		patient.profession = request.form.get('profession')
		patient.tel = request.form.get('tel')
		patient.address = request.form.get('address')
		patient.f_member_tel = request.form.get('f_member_tel')
		patient.family_history = request.form.get('family_history')
		patient.operation_history = request.form.get('operation_history')
		patient.injured_history = request.form.get('injured_history')
		patient.irritability_history = request.form.get('irritability_history')

		patient.diagnosis = request.form.get('diagnosis')
		patient.targeted_therapy = request.form.get('targeted_therapy')
		patient.radiotherapy = request.form.get('radiotherapy')
		patient.state_after_radiotherapy = request.form.get('state_after_radiotherapy')
		patient.drug_treatment_plan = request.form.get('drug_treatment_plan')
		patient.state_after_drugtreament = request.form.get('state_after_drugtreament')
		patient.clinical_stage = request.form.get('clinical_stage')
		patient.patient_statement = request.form.get('patient_statement')
		patient.image_result = request.form.get('image_result')
		patient.pathological_result = request.form.get('pathological_result')
		patient.pathological_grade = request.form.get('pathological_grade')
		patient.pathological_examination_result = request.form.get('pathological_examination_result')
		patient.genetic_examination_result = request.form.get('genetic_examination_result')
		patient.tumor_marker_result = request.form.get('tumor_marker_result')
		patient.operation_time = request.form.get('operation_time')
		patient.operation_type = request.form.get('operation_type')
		patient.operation_degree = request.form.get('operation_degree')
		patient.lymph_state = request.form.get('lymph_state')
		patient.diagnostic_time = request.form.get('diagnostic_time')
		patient.dead = request.form.get('dead')
		patient.death_time = request.form.get('death_time')
		patient.cause_of_death = request.form.get('cause_of_death')

		db.session.add(patient)
		db.session.commit()
	return render_template('patient_info.html')


@main.route('/patient_edit', methods=['GET', 'POST'])
def patient_edit():
	return render_template('patient_edit.html')

@main.route('/table', methods=['GET', 'POST'])
def table():
	plist = Patient.query.all()
	jlist = []
	for p in plist:
		l = {
			"name": p.name, 
			"admission_num": p.admission_num,
			"dead": p.dead,
			"cancer": p.cancer,
			"id": p.id,
			"sample_name": p.sample_name,
			"expdata_exist": p.expdata_exist,
			"refdata_exist": p.refdata_exist,
			"public": p.public
			}
		jlist.append(l)
	return jsonify(jlist)

@main.route('/upload_exdata', methods=['GET', 'POST'])
def upload_exdata():
	return render_template('upload_exdata.html')

@main.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
	return render_template('file_upload.html')


@main.route('/file_pinfo', methods=['GET', 'POST'])
def file_pinfo():
	save_id = request.form.get("save_id")
	patient = Patient.query.filter_by(id=save_id).first()
	l = {
		"name":patient.name,
		"admission_num": patient.admission_num,
		"idnum": patient.idnum,
		"doctor_email": patient.doctor_email
		}
	return jsonify(l)

@main.route("/biofiles", methods=['GET', 'POST'])
def biofiles():
	ALLOWED_EXTENSIONS = set(['txt'])

	def allowed_file(filename):
		return '.' in filename and \
				filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	ref_file = request.files['ref_data']
	exp_file = request.files['exp_data']
	save_id = request.form.get("saveid")
	p = Patient.query.filter_by(id=save_id).first()
	p.data_type = request.form.get('data_type')
	p.public = request.form.get('public')
	p.sample_name = request.form.get('sample_name')
	p.upl_name = request.form.get('upl_name')
	p.pro_name = request.form.get('pro_name')
	if ref_file and allowed_file(ref_file.filename):
		refname = save_id + "ref" + secure_filename(ref_file.filename)
		p.ref_data = os.path.join(current_app.config['UPLOAD_FOLDER'], refname)
		p.refdata_exist = "yes"
		ref_file.save(p.ref_data)

	if exp_file and allowed_file(exp_file.filename):
		expname = save_id + "exp" + secure_filename(exp_file.filename)
		p.exp_data = os.path.join(current_app.config['UPLOAD_FOLDER'], expname)
		p.expdata_exist = "yes"
		exp_file.save(p.exp_data)

	db.session.add(p)
	db.session.commit()
	return 'ok!'







