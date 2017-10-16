from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

login = Flask(__name__)

@login.route('/')

def html():
	return render_template('login.html')

@login.route('/checkPerson', methods=['POST'])
def checkPerson():
	idPass = dict(request.form.items())
	getID = idPass.get('id', None)
	if getID[0:5] == '59340':
		who = 'student'
	else:
		who = 'teacherofficer'
	person = str(who) + '.html'
	#print(idPass)
	return redirect(url_for('static', filename=person))

login.run(debug=True)
