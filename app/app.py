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
from FunctionAdd import Method
from Node_web import *
from keepHistory import *

app = Flask(__name__)

keepID = keepID()
keepHistory = keepHistory()

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

	conn = sqlite3.connect('IDPassStudent.db')
	countID = 0
	countPass = 0
	atRow = 0
	with conn:
		cur = conn.cursor()
		cur.execute("SELECT * FROM IDPASS")
		rows = cur.fetchall()
		countRow = 0
		for row in rows:
			countRow += 1
			for i in range(countRow):
				for row in rows[i]:
					if str(row) == getID:
						countID += 1
						atRow = i
						break;
					else:
						countID += 0
		for row in rows[atRow]:
				if str(row) == getPassword:
					countPass += 1
					break;
				else:
					countPass += 0
	#print(countID)
	#print(countPass)
	if countID > 1 and countPass == 1:
		m = Method(getID)
		name = m.cp_name()
		print(name)
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', id_user=getID, name_user=name )
	elif countID == 2 and countPass == 0:
		print('your password is incorrect')
	else:
		return render_template('homeTeacherofficer.html')
	conn.close()

@app.route('/menubar', methods=['POST'])
def menubar():
	getMenubar = request.form['click']
	print(getMenubar)
	getID = keepID.ID
	#keepID.Print_ID()
	m = Method(getID)
	name = m.cp_name()

	profile = [{'name':m.cp_name(),'birthD':m.cp_date(),'birthP':m.cp_birth(),'nation':m.cp_nation(),'edu':m.cp_edu(),'dis':m.cp_disease(),'relative':m.cp_relative(),'phoneEmer':m.cp_PhforEmer(),'cont':m.cp_Phstu(),'address':m.cp_address(),'email':m.cp_email()}]
	academic = [None]
	activity = [None]

	if getMenubar == 'PROFILE':
		keepHistory.keep_page('profile.html', profile)
		#return render_template('profile.html', name_user=name, nation=nation, dis=dis, relative=relative, phoneEmer=phoneEmer, birthD=birthD, birthP=birthP, cont=cont, address=address, email=email)
		return render_template('profile.html', name_user=name, page=profile)
	if getMenubar == 'ACADEMIC':
		keepHistory.keep_page('AcademicStudent.html', academic)
		return render_template('AcademicStudent.html', name_user=name, page=academic)
	if getMenubar == 'WORK&EXPERIENCE':
		keepHistory.keep_page('activity.html', activity)
		return render_template('activity.html', name_user=name, page=activity)
	if getMenubar == 'home_icon':
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', id_user=getID, name_user=name )
	if getMenubar == 'print_icon':
		print(getMenubar)
	if getMenubar == 'loguot_icon':
		print(getMenubar)
	if getMenubar == 'back':
		print(getMenubar)
		keepHistory.print_listPage()
		return render_template(keepHistory.history(),id_user=getID, name_user=name, page=keepHistory.Value_page())

@app.route('/printer', methods=['POST'])
def test():
	printer = request.form['click']
	print(printer)

@app.route('/selectTerm', methods=['POST'])
def selectTerm():
	getSelectTerm = request.form['click']
	print(getSelectTerm)

@app.route('/moreinfo', methods=['POST'])
def moreinfo():
	getMoreinfo = request.form['click']
	getID = keepID.ID
	m = Method(getID)
	name = m.cp_name()
	if getMoreinfo == 'MORE INFO>>':
		return render_template('dataactivity.html', name_user=name)

@app.route('/editInfo', methods=['POST'])
def editInfo():
	getEditInfo = request.form['click']
	getID = keepID.ID
	m = Method(getID)
	name = m.cp_name()
	if getEditInfo == 'EDIT':
		return render_template('edit-your-infomation.html', name_user=name)

@app.route('/editAc', methods=['POST'])
def editAc():
	getEditAc = request.form['click']
	getID = keepID.ID
	m = Method(getID)
	name = m.cp_name()
	if getEditAc == 'EDIT':
		return render_template('edit-activity.html', name_user=name)

'''@app.route('/test', methods=['POST'])
def test():
	getTest = request.form['click']
	print(getTest)'''

app.run(debug=True)
