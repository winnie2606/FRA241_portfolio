from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import sqlite3
import sys

login = Flask(__name__)

@login.route('/')

def html():
	return render_template('login.html')

@login.route('/checkPerson', methods=['POST'])
def checkPerson():
	idPass = dict(request.form.items())
	getID = idPass.get('id', None)
	getPassword = idPass.get('pass', None)

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
	print(countID)
	print(countPass)
	if countID == 2 and countPass == 1:
		who = 'student'
	elif countID == 2 and countPass == 0:
		who = 'incorrect'
		print('your password is incorrect')
	else:
		who = 'teacherofficer'
	person = str(who) + '.html'
	conn.close()
	return redirect(url_for('static', filename=person))

login.run(debug=True)
