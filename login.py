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

<<<<<<< HEAD
login.run(debug=True)
=======
app.run(debug=True)
#pairtest #PopTest
>>>>>>> 63bd0866ddf7c5fa2dcec8351d7b7ca9af1abd07
