from flask import render_template
from app import app
@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'jerh'}
    return render_template('index.html', title='Home',user=user)
@app.route('/fet.html')
def fet():
    return render_template('fet.html', title='Flat Earth Tours')
@app.route('/so.html')
def so():
    return render_template('so.html', title='Snake Oils')