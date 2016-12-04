from app import app
import os.path
import socket
import json
import urllib2
from flask import render_template, flash, redirect
from flask_autoindex import AutoIndex

# import sys
# sys.path.append('../python')
# import axislib

files_index = AutoIndex(app, os.path.curdir + '/app/reports', add_url_rules=False)

@app.route("/")
@app.route("/index")
def index():
    #return "Hello from " + socket.gethostname()
	return render_template('index.html', title='Home')

@app.route('/reports/', defaults={'path': ''})
@app.route('/reports/<path:path>')
def autoindex(path):
    return files_index.render_autoindex(path)
