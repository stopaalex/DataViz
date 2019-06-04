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

def createNewUser(req):
    createNewUserData = json.loads(req.get_data().decode('utf8'))
    # pwHash = sha256_crypt.hash(createNewUserData['pwPreHash'])
    pwHashBytes = base64.b64encode(bytes(createNewUserData['pwPreHash'], 'utf8'))
    pwHash = str(pwHashBytes, 'utf8')
    email = createNewUserData['email']
    token = ''

    if createNewUserData['keepLoggedIn']:
        alphabet = string.ascii_letters + string.digits 
        token = ''.join(secrets.choice(alphabet) for i in range(128))

    conn = None
    createNewUserDataReturn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='day2day',
                                user='astopa',
                                password='password')
        cur = conn.cursor()

        # create the sql commands to:
        # insert the new data into the users field
        createNewUserCommand = '''
            INSERT INTO {table} ({columns},password) VALUES ({values},'{pwHash}');
        '''.format(table=createNewUserData['table'], columns=createNewUserData['columns'], values=createNewUserData['values'], pwHash=pwHash)
        # then full that data back out to ensure it was pushed correctly
        checkCreateNewUserCommand = '''
            SELECT * FROM users WHERE email='{email}'
        '''.format(email=email)
        # get the columns to match up to the data
        getColumnKeysCommand = '''
            SELECT column_name FROM information_schema.columns WHERE table_name='{table}'
        '''.format(table=createNewUserData['table'])
        # execute insert
        cur.execute(createNewUserCommand)
        # execute the check
        cur.execute(checkCreateNewUserCommand)
        createNewUserDataReturnTemp = cur.fetchall()
        # turn the returned data into the list correctly
        if len(createNewUserDataReturnTemp) > 0:
            createNewUserDataReturn = [list(i) for i in createNewUserDataReturnTemp]
        else:
            createNewUserDataReturn = 'ERROR: Profile not created correctly...'
            # execute the get columns
        cur.execute(getColumnKeysCommand)
        getTableColumnsReturnTemp = cur.fetchall()
        # turn the columns into a list
        getTableColumnsReturn = []        
        for x in range(len(getTableColumnsReturnTemp)):
            column = str(getTableColumnsReturnTemp[x]).replace('(', '').replace("'", '').replace(')', '').replace(',', '')
            getTableColumnsReturn.append(column)
        # add the data into the list so it's formatted like a csv
        createNewUserDataReturn.insert(0, getTableColumnsReturn)
        # get the id of the created data
        cur.execute("SELECT id FROM users WHERE email='{email}'".format(email=email))
        tokenUserID = cur.fetchall()
        # insert the token into the user tokens field to match the 
        keepLoggedInCommand = '''
            INSERT INTO user_tokens (user_id, token) VALUES('{id}','{token}')
        '''.format(id=tokenUserID[0][0], token=token)

        cur.execute(keepLoggedInCommand)

        if createNewUserData['keepLoggedIn']:
            createNewUserDataReturn[0][-1] = 'token'
            createNewUserDataReturn[1][-1] = token
        else:
            createNewUserDataReturn[0][-1] = 'token'
            createNewUserDataReturn[1][-1] = 'false'

        cur.close()
        conn.commit()
    # exceptions and finally statements 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        createNewUserDataReturn = 'ERROR: ' + str(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return createNewUserDataReturn

    # return ''
