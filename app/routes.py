from app import app
from flask import render_template, request
import requests as r
from random import randrange

from app.services import CharDict, Episode
from .forms import Epform



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rm', methods=['GET', 'POST'])
def rm():
    new = CharDict()
    new.add_rand_char()
    epform = Epform()
    epi = Episode()
    if request.method == 'POST':
        print(epform.data)
        epi.load_ep(epform.data['ep_choice'])
        print(epi.chars)
        # epi.view_eps()
        return render_template('rm.html', new=new, epi=epi, epform=epform)
    # epi.load_ep(8)
    return render_template('rm.html', new=new, epi=epi, epform=epform)
