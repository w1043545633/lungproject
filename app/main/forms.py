# -*- coding: UTF-8 -*-  

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, NumberRange
from wtforms import ValidationError

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PatientBaseInfoForm(Form):
	name = StringField("姓名：", validators=[Required()])
	birth_date = StringField("出生日期：", validators=[Required()],
							render_kw={"placeholder": "1970/01/01"})
	gender = RadioField('性别：', choices=[('男', '男'), ('女', '女')], 
						validators=[Required()])
	admission_num = StringField('住院号：', validators=[Required()])
	idnum = IntegerField('身份证号：', validators=[Required(), NumberRange(min=18, max=18)])
	hospital = SelectField('选择医院：', choices=[
				('黄陂妇幼保健院', '黄陂妇幼保健院'),
				('武汉市中南医院', '武汉市中南医院'),
				('湖北省肿瘤医院', '湖北省肿瘤医院'),
				('武汉市协和医院', '武汉市协和医院'),
				('武汉市同济医院', '武汉市同济医院')])
	cancer = SelectField('癌症分型', choices=[
				('肺鳞癌', '肺鳞癌'),
				('肺腺癌', '肺腺癌'),
				('小细胞肺癌', '小细胞肺癌'),
				('大细胞肺癌', '大细胞肺癌'),
				('类癌', '类癌'),
				('细支气管肺泡癌', '细支气管肺泡癌'),
				('其他', '其他')])
	smoke = SelectField('吸烟史', choices=[
				('无', '无'),
				('五年以下', '五年以下'),
				('5-10年', '5-10年'),
				('10-20年', '10-20年'),
				('20-30年', '20-30年'),
				('30-40年', '30-40年'),
				('40年以上', '40年以上')])
	intemperance = SelectField('酗酒史', choices=[
				('无', '无'),
				('五年以下', '五年以下'),
				('5-10年', '5-10年'),
				('10-20年', '10-20年'),
				('20-30年', '20-30年'),
				('30-40年', '30-40年'),
				('40年以上', '40年以上')])
	take_drug = SelectField('吸毒史', choices=[
				('无', '无'),
				('五年以下', '五年以下'),
				('5-10年', '5-10年'),
				('10-20年', '10-20年'),
				('20-30年', '20-30年'),
				('30-40年', '30-40年'),
				('40年以上', '40年以上')])
	other_bad_habits = StringField('其他不良生活习惯史')
	doctor_email = StringField('主治医师邮箱', validators=[Required()])
	national = StringField('民族', validators=[Required()])
	profession = StringField('职业', validators=[Required()])
	tel = StringField('联系方式', validators=[Required()])
	address = StringField('住址', validators=[Required()])
	f_member_tel = StringField('家属电话', validators=[Required()])
	family_history = StringField('家族病史', validators=[Required()])
	operation_history = StringField('手术史', validators=[Required()])
	injured_history = StringField('外伤史', validators=[Required()])
	irritability_history = StringField('食物药物过敏史', validators=[Required()])

	diagnosis = TextAreaField('诊断描述', validators=[Required()])
	targeted_therapy = TextAreaField('靶向治疗', validators=[Required()])
	radiotherapy = TextAreaField('放疗方案', validators=[Required()])
	state_after_radiotherapy = TextAreaField('放疗后状态', validators=[Required()])
	drug_treatment_plan = TextAreaField('药物治疗方案', validators=[Required()])
	state_after_drugtreament = TextAreaField('药物治疗后状态', validators=[Required()])
	clinical_stage = TextAreaField('临床分期', validators=[Required()])
	patient_statement = TextAreaField('主述', validators=[Required()])
	image_result = TextAreaField('影像结果', validators=[Required()])
	pathological_result = TextAreaField('病理结果', validators=[Required()])
	pathological_grade = TextAreaField('病理分级', validators=[Required()])
	pathological_examination_result = TextAreaField('病理检测结果', validators=[Required()])
	genetic_examination_result = TextAreaField('基因检测结果', validators=[Required()])
	tumor_marker_result = TextAreaField('肿瘤标记物结果', validators=[Required()])
	operation_time = TextAreaField('手术时间', validators=[Required()])
	operation_type = TextAreaField('手术类型', validators=[Required()])
	operation_degree = TextAreaField('手术切除程度', validators=[Required()])
	lymph_state = TextAreaField('淋巴结清扫情况', validators=[Required()])
	diagnostic_time = StringField('确诊时间', validators=[Required()])
	dead = RadioField('是否死亡', choices=[(True, '是'), (False, '否')], 
						validators=[Required()])
	death_time = StringField('死亡时间', validators=[Required()])
	cause_of_death = TextAreaField('死亡原因', validators=[Required()])
	submit = SubmitField('提交')

