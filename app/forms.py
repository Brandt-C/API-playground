from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, RadioField

# form for selecting episode from all within API
class Epform(FlaskForm):
    ep_choice = SelectField('Select Episode', choices=[str(i) for i in range(1, 52 )], coerce=int, )
    submit = SubmitField("Build Episode")

# selecting from available locations
class Locform(FlaskForm):
    loc_choice = SelectField('Select Location', choices=[str(i) for i in range(1, 127)], coerce=int)
    submit = SubmitField("Build Location")

# modifications for bio section
class BioForm(FlaskForm):
    type_choice = RadioField("Techiness level", choices=["I'm NOT techy", "I'm Techy"], default="I'm NOT techy")
    l_choice = RadioField("Length", choices=['XS', 'TL;DR', 'Longer', 'Really Long'], default='XS')
    submit = SubmitField('Change')