from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
# from wtforms.validators import DataRequired

class Epform(FlaskForm):

    ep_choice = SelectField('Select Episode', choices=[str(i) for i in range(1, 52 )], coerce=int, )
    submit = SubmitField("Build Episode")

class Locform(FlaskForm):
    loc_choice = SelectField('Select Location', choices=[str(i) for i in range(1, 127)], coerce=int)
    submit = SubmitField("Build Location")