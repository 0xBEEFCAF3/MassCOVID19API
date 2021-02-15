#!/usr/bin/env python3.8

import pandas as pd
from pathlib import Path
import glob, os
from datetime import datetime, timedelta
import json

current_time = datetime.now() - timedelta(days=1)
formatedTime = str(current_time.strftime('%b')) + "-" + str(current_time.day) + "-" + str(current_time.year)

def generate_reports():
    report_obj = {}
    df = pd.ExcelFile('./reports/'+formatedTime+'.xlsx', engine='openpyxl')
    sheets = df.sheet_names
    jsonDump = {}
    for sheet in sheets:
        parsed_sheet = df.parse(sheet)
        jsonDump[sheet] = parsed_sheet.to_dict(orient='records')
    def dateConverter(o):
        if isinstance(o, datetime):
            return o.__str__()
    return str(json.dumps(jsonDump, default=dateConverter)).replace('NaN', '0')

# def write_report():
#     report = generate_reports()

print(generate_reports())