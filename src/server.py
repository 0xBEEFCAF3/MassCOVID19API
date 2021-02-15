#!/usr/bin/env python3.8


from flask import Flask
from convertReport import generate_reports

app = Flask(__name__)

@app.route('/')
def get():
     return generate_reports()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
