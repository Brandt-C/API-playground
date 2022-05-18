from app import app
from flask import render_template
import requests as r

@app.route('/')
def home():
    return render_template('index.html')