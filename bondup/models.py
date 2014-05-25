from bondup import db

events_people = db.Table('events_people',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

events_tags = db.Table('events_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

people_tags = db.Table('people_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    loc = db.Column(db.String(64))
    particips = db.relationship('Person',
        secondary=events_people,
        backref=db.backref('events', lazy='dynamic')
    )
    tags = db.relationship('Tag',
        secondary=events_tags,
        backref=db.backref('events', lazy='dynamic')
    )

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    flex = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    tags = db.relationship('Tag',
        secondary=people_tags,
        backref=db.backref('people', lazy='dynamic')
    )

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
