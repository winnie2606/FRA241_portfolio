from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

test = Flask(__name__)

activity = {'name1':['advisor1', 'date1', 'type1', 'des1', 'file1'],
            'name2':['advisor2', 'date2', 'type2', 'des2', 'file2']}

@test.route('/')
def html():
	return render_template('test.html', activity = activity)

test.run(debug=True)
