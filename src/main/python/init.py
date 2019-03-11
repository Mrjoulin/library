from flask import Flask
from db import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

