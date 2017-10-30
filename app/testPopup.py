from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

test = Flask(__name__)


@test.route('/')
def html():
	return render_template('testPopup.html')

@test.route('/getPopup', methods=['POST'])
def getPopup():
<<<<<<< HEAD
    getPopup = request.form['text1']
=======
    getPopup = request.form['save']
>>>>>>> 392d70898aeeafdfd4c8bb3a3a862abe32f622e5
    print(getPopup)
test.run(debug=True)
