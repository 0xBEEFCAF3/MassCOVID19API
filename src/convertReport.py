#!/usr/bin/python

import pandas as pd
from pathlib import Path
import glob, os
from datetime import datetime

current_time = datetime.now()
formatedTime = str(current_time.month) + "-" + str(current_time.day) + "-" + str(current_time.year)


def get_report_files_names():
    old_dir = os.getcwd()
    os.chdir(old_dir + '/reports')
    sorted_dirs = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
 
    os.chdir(old_dir)

    return  sorted_dirs

def get_date_from_name(name):
    ##Format on mass.gov is -- COVID-19-Dashboard-Files-mm-dd-yyyy -> extract the date
    return "-".join(name.split('-')[4:])

def get_csv_names():
    os.chdir("reports/COVID-19-Dashboard-Files-"+formatedTime)
    return [f for f in glob.glob("*.csv")]

def generate_reports():
    report_obj = {}
    for report in get_csv_names():
        report_obj[report] = generate_report(report)

def generate_report(file_name):

    reports = []

    df = pd.read_csv(file_name)
    return df.to_json()

def pickle_report_object(obj):
   pickle.dump(obj, 'pickle/current_report') 
