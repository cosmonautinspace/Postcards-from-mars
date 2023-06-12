from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, StringField
from wtforms.validators import DataRequired, InputRequired

class getpicture(FlaskForm):
    pictureDate = StringField('Picture Date (YYYY-M-D)', validators=[DataRequired()])
    submit = SubmitField('Get Picture')