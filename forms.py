from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class getpicture(FlaskForm):
    rover = SelectField('Rover', choices=[('Curiosity','Curiosity'),('Opportunity','Opportunity  (Not Tested)'),('Spirit','Spirit (Not Tested)')], validators=[DataRequired()])
    pictureDate = DateField('Date', format="%Y-%m-%d", validators=[DataRequired()])
    submit = SubmitField('Get Picture')