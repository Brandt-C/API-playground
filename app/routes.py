from app import app
from flask import render_template
import requests as r
from random import randrange

from app.services import CharDict



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rm')
def rm():
    new = CharDict()
    new.add_rand_char()
    
    return render_template('rm.html', new=new)
