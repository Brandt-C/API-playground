from app import app
from flask import render_template, request
import requests as r
from random import randrange

from app.services import CharDict, Episode, Location
from .forms import Epform, Locform



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rm', methods=['GET', 'POST'])
def rm():
    new = CharDict()
    new.add_rand_char()
    epform = Epform()
    epi = Episode()
    locform = Locform()
    loc = Location()
    if request.method == 'POST':
        
        epi.load_ep(epform.data['ep_choice'])
        loc.load_loc(locform.data['loc_choice'])
        # epi.view_eps()
        return render_template('rm.html', new=new, epi=epi, epform=epform, locform=locform, loc=loc)
    # epi.load_ep(8)
    return render_template('rm.html', new=new, epi=epi, epform=epform, locform=locform, loc=loc)
