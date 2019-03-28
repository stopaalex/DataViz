'''
astopa

'''
# create flask app

from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api


from random import *

import json, csv, os.path, datetime

import pandas as pd

from api import authorize

# 
# define the app
app = Flask(__name__)

# 
# serve up the index.html file
@app.route("/")
def index():
    return send_file('templates/index.html')

@app.route('/test', methods=['POST'])
def test():

     auth = authorize.authUser()
     return auth

if __name__ == '__main__':
     app.run(port=8080)