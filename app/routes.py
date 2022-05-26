from app import app
from flask import render_template
import requests as r
from random import randrange

from app.services import CharDict, EpisodeBuilder



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rm')
def rm():
    new = CharDict()
    new.add_rand_char()
    epi = EpisodeBuilder()
    epi.load_ep(8)
    epi.view_eps()
    
    return render_template('rm.html', new=new, epi=epi)
