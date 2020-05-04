
from flask import Flask
from convertReport import generate_reports

app = Flask(__name__)

@app.route('/')
def get():
     return generate_reports()


