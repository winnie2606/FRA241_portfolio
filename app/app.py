from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from Profile import Profile
import sqlite3
import sys

app = Flask(__name__)

@app.route('/')
def html():
	return render_template('login.html')

@app.route('/getIDPass', methods=['POST'])
def getIDPass():
	idPass = dict(request.form.items())
	return(idPass)
@app.route('/checkPerson', methods=['POST'])
def checkPerson():
	getID = getIDPass().get('id', None)
	getPassword = getIDPass().get('pass', None)

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
		pro = Profile('{}.db'.format(getID))
		conne = pro.conne()
		conne.row_factory = sqlite3.Row
		cursor = conne.cursor()
		cursor.execute("SELECT * FROM PROFILE")
		roww = cursor.fetchone()
		findname = pro.name(roww)
		return render_template('homeStudent.html', id_user = getID, name_user = findname)
	elif countID == 2 and countPass == 0:
		who = 'incorrect'
		print('your password is incorrect')
	else:
		return render_template('homeTeacherofficer.html', id_user = getID)
	#person = str(who) + '.html'
	conn.close()

	#return render_template('homeStudent.html', id_user = getID)
@app.route('/proflies', methods=['POST'])
def profiles():
	return render_template('profile.html')
app.run(debug=True)
