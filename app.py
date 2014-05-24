import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'test.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='pass'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def home():
    return 'Welcome.'

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('person/<int:person_id>')
def show_person(person_id):
    db = get_db()
    cur = db.execute('SELECT iden, age FROM people WHERE id = ?', person_id)
    person = cur.fetchall()
    return render_template('show_person.html', person=person)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
