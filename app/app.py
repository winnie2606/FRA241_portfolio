from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import sqlite3
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from keepID import *
from getDatabase import *
from Node_web import *
from keepHistory import *
from pullData import *
from editProfile import *
from editActivity import *
from saveText import *

app = Flask(__name__)

keepID = keepID()
keepHistory = keepHistory()
pullData = pullData()
editProfile = editProfile()
editActivity = editActivity()
saveText = saveText()

@app.route('/')
def html():
	return render_template('login.html')

@app.route('/getIDPass', methods=['POST'])
def getIDPass():
	idPass = dict(request.form.items())
	return(idPass)

@app.route('/getID', methods=['POST'])
def getID():
	getID = getIDPass().get('id', None)
	#keepID.ID = getID
	return(getID)

@app.route('/getPass', methods=['POST'])
def getPass():
	getPassword = getIDPass().get('pass', None)
	#keepID.Password = getPassword
	return(getPassword)

@app.route('/checkPerson', methods=['POST'])
def checkPerson():
	getID = getIDPass().get('id', None)
	getPassword = getIDPass().get('pass', None)
	keepID.ID = getID
	keepID.Password = getPassword
	print (getID)
	print (getPassword)
	check = Check()

	if check.S_check(getID,getPassword) :
		print (getID)
		re = return_Method(getID)
		name = re.name()
		keepID.Name = name
		print(keepID.Name)
		keepHistory.keep_page('homeStudent.html', None )
		return render_template('homeStudent.html', id_user=getID, name=name)

	elif  check.T_check(getID,getPassword):
		re = return_Method(getID)
		name = re.t_name()
		keepID.Name = name
		keepHistory.keep_page('port_tea.html', None )
		return render_template('port_tea.html' , name = name )





'''---------------------------------------------------------------------------------------------------------------------------------------------------'''
""" Student """

@app.route('/menubar', methods=['POST'])
def menubar():
	getMenubar = request.form['click']
	print(getMenubar)
	getID = keepID.ID
	name = keepID.Name

	if getMenubar == 'PROFILE':
		keepHistory.keep_page('profile.html', pullData.Profile(getID))
		return render_template('profile.html', name=name, page=pullData.Profile(getID))
	if getMenubar == 'ACADEMIC':
		keepHistory.keep_page('AcademicStudent.html', pullData.Academic_term(getID),pullData.Academic_sum(getID))
		return render_template('AcademicStudent.html', name=name, page=pullData.Academic_term(getID), page2=pullData.Academic_sum(getID))
	if getMenubar == 'WORK&EXPERIENCE':
		keepHistory.keep_page('activity.html', pullData.Activity(getID))
		return render_template('activity.html', name=name, page=pullData.Activity(getID))
	if getMenubar == 'home_icon':
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', name=name, id_user=getID)
	if getMenubar == 'print_icon':
		keepHistory.keep_page('print_choose.html', pullData.Activity(getID))
		print(getMenubar)
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))
	if getMenubar == 'logout_icon':
		print(getMenubar)
		keepHistory.reset_keepHistory()
		keepID.reset_keepID()
		return render_template('login.html')
	if getMenubar == 'back':
		print(getMenubar)
		keepHistory.print_listPage()
		history = keepHistory.history()
		Value = keepHistory.Value_page()
		Value2 = keepHistory.Value2_page()
		if history == 'activity.html':
			Value = pullData.Activity(getID)
		return render_template(history,id_user=getID, name=name, page = Value, page2 = Value2)

@app.route('/printer', methods=['POST'])
def printer():
	printer = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	#keepID.Print_ID()

	keepHistory.keep_page('print_choose.html', pullData.Activity(getID))
	print(printer)
	return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/selectTerm', methods=['POST'])
def selectTerm():
	getSelectTerm = request.form['click']
	print(getSelectTerm)
	getID = keepID.ID
	name = keepID.Name
	if getSelectTerm == '1/2559':
		term = '1/2559'
	if getSelectTerm == '2/2559':
		term = '2/2559'
	if getSelectTerm == '1/2560':
		term = '1/2560'
	if getSelectTerm == '2/2560':
		term = '2/2560'
	return render_template('AcademicStudent.html', name=name, term=term, page=pullData.Academic_term(getID,term),page2=pullData.Academic_sum(getID,term))

@app.route('/moreinfo', methods=['POST'])
def moreinfo():
	getMoreinfo = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name
	print(getMoreinfo)

	for nameAct in getMoreinfo:
		for Act in pullData.Activity(getID):
			if Act["Name_Activity"] == nameAct :
				keepHistory.keep_page('dataactivity.html',Act)
				print (Act)
				return render_template('dataactivity.html', name=name, page= Act )
'''
	if getMoreinfo == 'MORE INFO>>':
		keepHistory.keep_page('dataactivity.html', pullData.Activity(getID))
		keepHistory.print_listPage()
		return render_template('dataactivity.html', name=name, page=pullData.Activity(getID))
'''

@app.route('/editInfo', methods=['POST'])
def editInfo():
	getEditInfo = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	if getEditInfo == 'EDIT':
		keepHistory.keep_page('edit-your-infomation.html', None)
		return render_template('edit-your-infomation.html', name=name)

@app.route('/editAcButton', methods=['POST'])
def editAcButton():
	getEditAc = dict(request.form.items())
	print(getEditAc)
	getID = keepID.ID
	name = keepID.Name

	for nameAct in getEditAc:
		for Act in pullData.Activity(getID):
			if Act["Name_Activity"] == nameAct :
				keepHistory.keep_page('dataactivity.html',Act)
				return render_template('edit-activity.html', name=name, page= Act["Name_Activity"] )

'''
	if getEditAc == 'EDIT':
		keepHistory.keep_page('edit-activity.html',None)
		return render_template('edit-activity.html', name=name) '''

@app.route('/getEditInfo', methods=['POST'])
def getEditInfo():
	getEditInfo = dict(request.form.items())
	print(getEditInfo)
	getID = keepID.ID
	#keepID.Print_ID()

	editProfile.edit(getID,getEditInfo)

	re = return_Method(getID)
	name = re.name()
	keepID.Name = name

	history = keepHistory.history()

	return render_template(history , name=name, page=pullData.Profile(getID))

@app.route('/getEditAc', methods=['POST'])
def getEditAc():
	getEditAc = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name

	print(getEditAc)

	for nameAct in getEditAc:
		if nameAct != 'type' and nameAct != 'photo'and nameAct != 'advisor'and nameAct != 'des' and nameAct != 'fileDoc' and nameAct != 'date':
			print(nameAct)
			Name_act = nameAct

	editActivity.add(getID,Name_act,getEditAc)

	for Act in pullData.Activity(getID):
		if Act["Name_Activity"] == Name_act :
			history = keepHistory.history()
			return render_template(history , name=name, page= Act)

@app.route('/checkBox', methods=['POST'])
def getCheckBox():
	getCheck = dict(request.form.items())
	print(getCheck)
	getCheckBox = request.form['click']
	print(getCheckBox)

	getID = keepID.ID
	name = keepID.Name

	re = return_Method(getID)
	s = Get_Academic(getID,None)

	ProfileAndAcademic = []
	data = {'name':re.name(),'sur':re.surname(),'dateofbirth':re.date(),'nation':re.nation(),'gpax':'-','contact':'','phone':'','address':'','email':'','dis':'','birthplace':''}
	Activity = []

	if getCheck.get('gpax') == 'on':
		data['gpax'] = ''.join(s.get_GPAX())
		print('select gpax')
	if getCheck.get('contact') == 'on':
		data['contact'] = "CONTACT"
		data['phone'] = "PHONE : " + re.Phonestu()
		data['address'] = "ADDRESS : " +  re.address()
		data['email'] = "EMAIL : " + re.email()
		print('select contact')
	if getCheck.get('congenital disease') == 'on':
		data['dis'] = "CONGENITAL DISEASE : " + ','.join(re.disease())
		print('select congenital disease')
	if getCheck.get('birthplace') == 'on':
		data['birthplace'] = "BIRTH PLACE : " + re.birth()
		print('select birthplace')

	ProfileAndAcademic.append(data)

	DataActivity = pullData.Activity(getID)
	for Act in DataActivity:
		nameAct = Act["Name_Activity"]
		if getCheck.get(nameAct) == 'on' :
			Activity.append(Act)

	if getCheckBox == 'DONE':
		print(ProfileAndAcademic)
		print(Activity)
		keepHistory.keep_page('printdata.html', ProfileAndAcademic,Activity)
		return render_template('printdata.html',id_user=getID, name=name, page=ProfileAndAcademic , page2 = Activity )

@app.route('/selectall', methods=['POST'])
def selectall():
	getSelectall = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if getSelectall == 'SELECTALL':
		return render_template('print_choose_selectall.html', name=name, page=pullData.Activity(getID))
	if getSelectall == 'UNSELECTALL':
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/getAddAcButton', methods=['POST'])
def getAddAcButton():
	getAddAc = request.form['click']
	print(getAddAc)
	getID = keepID.ID
	name = keepID.Name
	if getAddAc == 'ADD':
		keepHistory.keep_page('activity.html', pullData.Activity(getID))
		return render_template('add-activity.html', name=name)

@app.route('/getAddAc', methods=['POST'])
def geAddAc():
	getAddAc = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name
	print(getAddAc)

	editActivity.edit(getID,getAddAc)

	history = keepHistory.history()

	return render_template(history, name=name, page=pullData.Activity(getID))

@app.route('/getPrindataButton', methods=['POST'])
def getPrindataButton():   												#--------- save text -----------
	button = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if button == 'SAVE':
		print('save')
		profile = keepHistory.Value_page()
		activity = keepHistory.Value2_page()
		print(profile)
		print(activity)

		saveText.create(getID,profile,activity)

		history = keepHistory.history()
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', name=name, id_user=getID)
	if button  == 'EDIT':
		print('edit')
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/getPopup', methods=['POST'])
def getPopup():
	getpopup = request.form['popup']
	print(getpopup)
	if getpopup == 'Exit':
		keepHistory.reset_keepHistory()
		keepID.reset_keepID()
		return render_template('login.html')

@app.route('/getleave', methods=['POST'])
def getleave():
	getID = keepID.ID
	name = keepID.Name
	getleave = request.form['popup']
	print(getleave)
	if getleave == 'YES':
		keepHistory.print_listPage()
		history = keepHistory.history()
		if history == 'activity.html':
			Value = pullData.Activity(getID)
			return render_template(history,id_user=getID, name=name, page = Value)
		if history == 'dataactivity.html':
			Value = keepHistory.Value_page()
			return render_template(history,id_user=getID, name=name, page = Value)

'''end student'''

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

""" Teacher """

@app.route('/menubarTeacher', methods=['POST'])
def getMenubarTeacher():
	getmenubar = request.form['click']
	print(getmenubar)
	getID = keepID.ID
	name = keepID.Name

	if getmenubar == 'back':
		print('back')
		history = keepHistory.history()
		Value = keepHistory.Value_page()
		Value2 = keepHistory.Value2_page()
		return render_template(history,id_user=getID, name=name, page = Value, page2 = Value2)

	if getmenubar == 'home':
		print('home')
		keepHistory.keep_page('port_tea.html', None)
		return render_template('port_tea.html',name=name)

@app.route('/gethome', methods=['POST'])
def gethome():
	gethome = request.form['click']
	print(gethome)
	getID = keepID.ID
	name = keepID.Name

	if gethome == 'frab':
		print('frab')
		return render_template('total_frab.html', name=name)
	if gethome == 'grade':
		print('add grade')
		return render_template('add_grade.html', name=name)

@app.route('/getFrab', methods=['POST'])
def frab():
	frab = request.form['click']
	print(frab)
	getID = keepID.ID
	name = keepID.Name

	if frab == '1':
		print('1')
		frab = '1'
		return render_template('nametea.html', name=name, frab=frab)
	if frab == '2':
		print('2')
		frab = '2'
		return render_template('nametea.html', name=name, frab=frab)
	if frab == '3':
		print('3')
		frab = '3'
		return render_template('nametea.html', name=name, frab=frab)
	if frab == '4':
		print('4')
		frab = '4'
		return render_template('nametea.html', name=name, frab=frab)

@app.route('/getView', methods=['POST'])
def view():
	view = dict(request.form.items())
	print(view)
	getID = keepID.ID
	name = keepID.Name
	return render_template('teacherViewProfile.html', name=name, frab=frab)

@app.route('/selectView', methods=['POST'])
def seect():
	select = request.form['click']
	print(select)
	getID = keepID.ID
	name = keepID.Name

	if select == 'PROFILE':
		print('profile')
		return render_template('teacherViewProfile.html', name=name)
	if select == 'ACADEMIC':
		print('academic')
		return render_template('teacherViewAcademic.html', name=name)
	if select == 'WORK&EXPERIENCE':
		print('activity')
		return render_template('teacherViewActivity.html', name=name)


app.run(debug=True)
