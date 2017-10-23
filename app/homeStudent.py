from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import sqlite3
import sys

homeStudent = Flask(__name__)

@homeStudent.route('/')

print('eiei')

homeStudent.run(debug=True)
