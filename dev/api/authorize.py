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
    if os.path.exists('/db/users.table.csv'):
        print('there is a table')
        # read in the csv to see if we need to reauth them
    else:
        print('new user')
        print('navigate to login/user')
        # create the auth table with the users creds

    return 'hit the authorize function'