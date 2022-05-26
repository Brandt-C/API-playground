from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
# from wtforms.validators import DataRequired

class Epform(FlaskForm):

    ep_choice = SelectField('Select Episode', choices=[str(i) for i in range(1, 51 )], coerce=int, )
    submit = SubmitField()
