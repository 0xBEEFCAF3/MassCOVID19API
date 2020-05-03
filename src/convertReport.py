#!/usr/bin/python

import pandas as pd
from pathlib import Path
import glob, os
from datetime import datetime
import json

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

def format_csv_file_name(name):
    return name.replace(' ', '').replace('.csv', '')

def get_csv_names(path):
    old_dir = os.getcwd()
    os.chdir(old_dir + '/reports/' + path)
    sorted_dirs =  [f for f in glob.glob("*.csv")] 
    os.chdir(old_dir)
    return sorted_dirs

def generate_reports():
    report_obj = {}
    for report_path in get_report_files_names():
        formated_date = get_date_from_name(report_path)
        report_obj[formated_date] = {}
        for report_aspect in get_csv_names(report_path):
            report_obj[formated_date][format_csv_file_name(report_aspect)] = generate_report(report_path, report_aspect)
    return str(json.dumps(report_obj)).replace('NaN', '0')

def generate_report(path, file_name):
    df = pd.read_csv('./reports/' + path + '/' +file_name)
    return df.to_dict('records')

def pickle_report_object(obj):
   pickle.dump(obj, 'pickle/current_report') 
