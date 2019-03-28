from flask import Flask, flash, redirect, render_template, send_file, request, session, abort
from flask_restful import Resource, Api


from random import *

import json, csv, os.path, datetime

import pandas as pd


def authUser():
    if os.path.exists('db/auth/auth.csv'):
        print('returning user')
        # read in the csv to see if we need to reauth them
    else:
        print('new user')
        # create the auth table with the users creds


    return 'hit the authorize function'