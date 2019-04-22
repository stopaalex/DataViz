'''
Start importing all required python dependencies
'''
from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api


from random import *

import json, csv, os.path, datetime

import pandas as pd
'''
Finish importing all required python dependencies
'''


def authUser():
    returnText = ''
    if os.path.exists('/db/users.table.csv'):
        returnText = 'there is a table'
        print('there is a table')
        # read in the csv to see if we need to reauth them
    else:
        returnText = 'there is no table, create table and navigate to create login page'
        print('there is no table, create table')
        print('navigate to login/user')
        # create the auth table with the users creds

    return returnText