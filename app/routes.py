from app import app
from flask import render_template, request


from app.services import CharDict, Episode, Location, Bio
from .forms import BioForm, Epform, Locform


# landing/home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = BioForm()
    bio = Bio()
    bb = bio.nt['xs']
    if request.method == 'POST':
        bb = bio.convert(form.data['type_choice'], form.data['l_choice'])
        return render_template('index.html', form=form, bio=bio, bb=bb)
    return render_template('index.html', form=form, bio=bio, bb=bb)

# rick/morty API page
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
        return render_template('rm.html', new=new, epi=epi, epform=epform, locform=locform, loc=loc)
    return render_template('rm.html', new=new, epi=epi, epform=epform, locform=locform, loc=loc)

@app.route('/f1')
def f1():
    return render_template('f1.html')