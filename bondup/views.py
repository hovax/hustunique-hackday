from flask import render_template, url_for
from bondup import app
from bondup.models import Person

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/person/<int:person_id>')
def show_person(person_id):
    person = Person.query.filter_by(id=person_id).first()
    return render_template('show_person.html', person=person)

@app.route('/search')
def search():
    return app.send_static_file('Search.html')
