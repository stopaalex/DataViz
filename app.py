'''
astopa

'''
# create flask app

'''
Start importing all required python dependencies
'''
from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api
from passlib.hash import sha256_crypt
import random, json, csv, os.path, datetime, secrets, string
import pandas as pd
# import api files
from api import postData, loginUser
'''
Finish importing all required python dependencies
'''

# define the app
app = Flask(__name__)

# serve up the index.html file
@app.route("/")
def index():
    return send_file('templates/index.html')

@app.route("/post-create-new-user", methods=['POST'])
def api_create_user():
     api_createUserReturn = postData.createNewUser(request)
     return str(api_createUserReturn)

@app.route("/auth-login-user", methods=['POST'])
def api_login_user():
     api_loginUserReturn = loginUser.loginWithPW(request)
     return str(api_loginUserReturn)

@app.route("/auth-auto-login-user", methods=['POST'])
def api_auto_login_user():
     api_autoLoginUserReturn = loginUser.loginWithToken(request)
     return str(api_autoLoginUserReturn)

# @app.route('/test', methods=['POST'])
# def testdef():
#      asdf = test.test_def()
#      return asdf

if __name__ == '__main__':
     app.run(debug=True)