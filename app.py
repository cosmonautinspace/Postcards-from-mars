from flask import Flask, render_template, url_for, redirect, flash
from forms import getpicture
from functions import apiRequest
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = ''
api_key = ''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Cosmonautinspace')

@app.route('/postcards', methods = ['GET', 'POST'])
def postcard_home():
    form = getpicture()
    if form.validate_on_submit():
        apiRequest(api_key, form.pictureDate.data, form.rover.data)
        return redirect(url_for('postcards', rover=form.rover.data, pictureDate = form.pictureDate.data))
    else:
        flash(form.errors)
    return render_template('postcards_home.html', title='Home',form=form)

@app.route('/postcards/<string:rover>/<string:pictureDate>')
def postcards(rover,pictureDate):
    file = open(f'cache/{rover}/{pictureDate}.json')
    data =  json.load(file)
    file.close()
    return render_template('postcards.html', title=pictureDate, data=data)

if __name__ == '__main__':
    app.run(debug=True) 
