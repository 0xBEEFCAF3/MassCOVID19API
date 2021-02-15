#!/usr/bin/env python3.8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get():
     with open('./reports/daily_final.json', 'r') as f:
          return f.read()
