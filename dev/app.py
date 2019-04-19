'''
astopa

'''
# create flask app

'''
Start importing all required python dependencies
'''
from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api


from random import *

import json, csv, os.path, datetime

import pandas as pd

# import api
# import api.authorize
from api import authorize
'''
Finish importing all required python dependencies
'''

# define the app
app = Flask(__name__)

# serve up the index.html file
@app.route("/")
def index():
    return send_file('templates/index.html')

# AUTHORIZE USER
@app.route('/authorizeUser', methods=['POST'])
def authorizeUser():
     auth = authorize.authUser()
     return auth

if __name__ == '__main__':
     app.run(port=8080)