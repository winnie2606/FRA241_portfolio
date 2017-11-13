from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import os
from shutil import copyfile

from pathlib import Path


test = Flask(__name__)


@test.route('/')
def html():
	return render_template('upload.html')

@test.route('/getfile', methods=['POST'])
def getfile():

    getfile = request.form['photo']

    print(getfile)

    #find = 'mydir/' + str(getfile)
    path =  os.fsdecode(getfile)
    print(path)
    '''name = 'Copy' + str(getfile)
    to = 'C:/Users/' + str(os.getlogin()) + '/Desktop/' + name
    #copyfile(path, str(to))'''


test.run(debug=True)
