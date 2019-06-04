'''
astopa

'''
# create flask app

'''
Start importing all required python dependencies
'''
from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api
import json, csv, os.path, datetime, random, psycopg2
import pandas as pd
'''
Finish importing all required python dependencies
'''

def createUser(req):
    createUserData = getData = json.loads(req.get_data().decode('utf8'))
    print(createUserData)
    return''

    conn = None;
    getDataReturn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='day2yday',
                                user='postgres',
                                password='password')
        cur = conn.cursor()

        getDataCommand = 'SELECT ' + getData['columns'] + ' FROM ' + getData['table']
        print('----------')
        print('getDataCommand:')
        print(getDataCommand)

        cur.execute(getDataCommand)
        getDataReturnTemp = cur.fetchall()

        if len(getDataReturnTemp) > 0:
            getDataReturn = [list(i) for i in getDataReturnTemp]
        else:
            getDataReturn = 'No data'

        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='{table}'".format(table=getData['table']))
        getDataColsReturnTemp = cur.fetchall()
        getDataColReturn = []
                
        for x in range(len(getDataColsReturnTemp)):
            column = str(getDataColsReturnTemp[x]).replace('(', '').replace("'", '').replace(')', '').replace(',', '')
            getDataColReturn.append(column)

        getDataReturn.insert(0, getDataColReturn)
        
        print('----------')
        print('getDataReturn:')
        print(getDataReturn)

        # if logInUserReturn[0][3].lower() == logInCheckEmail.lower() and logInUserReturn[0][6] == logInCheckPassword:
        #     print('          SUCCESSFULLY LOGGED IN USER          ')
        # else:
        #     logInUserReturn = 'ERROR - Incorrect password, please enter another.'

        cur.close()
        conn.commit()
    # exceptions and finally statements 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        getDataReturn = error
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return getDataReturn

    # return ''