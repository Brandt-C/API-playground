from app import app
from flask import render_template
import requests as r
from random import randrange
from app.services import add_char


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/rm')
def rm():
    x = randrange(1, 826)
    add_char(x)
    return render_template('rm.html')
