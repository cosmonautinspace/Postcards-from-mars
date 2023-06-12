from flask import Flask, render_template, url_for, redirect, flash
from forms import getpicture
from functions import apiRequest
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
api_key = 'cVx8cdLFLJree03QdRHdhr4tfndlWfgA60SRDrTR'

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = getpicture()
    if form.validate_on_submit():
        apiRequest(api_key, form.pictureDate.data)
        return redirect(url_for('postcards', pictureDate = form.pictureDate.data))
    else:
        flash(form.errors)
    return render_template('home.html', title='Home',form=form)

@app.route('/postcards/<string:pictureDate>')
def postcards(pictureDate):
    file = open(f'cache/{pictureDate}.json')
    data =  json.load(file)
    file.close()
    return render_template('postcards.html', title=pictureDate, data=data)

if __name__ == '__main__':
    app.run(debug=True) 