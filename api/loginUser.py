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
import json, csv, os.path, datetime, random, psycopg2, secrets, string, base64
import pandas as pd
'''
Finish importing all required python dependencies
'''

def loginWithPW(req):
    loginUserData = json.loads(req.get_data().decode('utf8'))
    pwHashBytes = base64.b64encode(bytes(loginUserData['password'], 'utf8'))
    pwHash = str(pwHashBytes, 'utf8')
    email = loginUserData['email']
    token = ''

    if loginUserData['keepLoggedIn']:
        alphabet = string.ascii_letters + string.digits 
        token = ''.join(secrets.choice(alphabet) for i in range(128))

    conn = None
    loginUserDataReturn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='day2day',
                                user='astopa',
                                password='password')
        cur = conn.cursor()
        loginUserCommand = '''
            SELECT * FROM users WHERE email='{email}' AND password='{pwHash}'
        '''.format(email=email,pwHash=pwHash)

        cur.execute(loginUserCommand)
        loginUserDataReturnTemp = cur.fetchall()
        # turn the returned data into the list correctly
        if len(loginUserDataReturnTemp) > 0:
            loginUserDataReturn = [list(i) for i in loginUserDataReturnTemp]

            getColumnKeysCommand = '''
                SELECT column_name FROM information_schema.columns WHERE table_name='{table}'
            '''.format(table='users')
            cur.execute(getColumnKeysCommand)
            getColumnKeysReturnTemp = cur.fetchall()

            getColumnKeysReturn = []        
            for x in range(len(getColumnKeysReturnTemp)):
                column = str(getColumnKeysReturnTemp[x]).replace('(', '').replace("'", '').replace(')', '').replace(',', '')
                getColumnKeysReturn.append(column)
            # add the data into the list so it's formatted like a csv
            loginUserDataReturn.insert(0, getColumnKeysReturn)

            cur.execute("SELECT id FROM users WHERE email='{email}'".format(email=email))
            tokenUserID = cur.fetchall()
            # insert the token into the user tokens field to match the 
            keepLoggedInCommand = '''
                UPDATE user_tokens SET token='{token}' WHERE user_id='{id}'
            '''.format(id=tokenUserID[0][0], token=token)

            if loginUserData['keepLoggedIn']:
                loginUserDataReturn[0][-1] = 'token'
                loginUserDataReturn[1][-1] = token
            else:
                loginUserDataReturn[0][-1] = 'token'
                loginUserDataReturn[1][-1] = 'false'

            cur.execute(keepLoggedInCommand)
        else:
            loginUserDataReturn = 'ERROR: That email, password combination does not exist'

        cur.close()
        conn.commit()
    # exceptions and finally statements 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        loginUserDataReturn = 'error:' + error
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return loginUserDataReturn
            

def loginWithToken(req):
    return 'token'