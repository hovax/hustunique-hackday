DROP TABLE IF EXISTS events;

CREATE TABLE events (
  id int PRIMARY KEY,
  iden varchar(64) NOT NULL,
  startmoment timestamp with time zone NOT NULL,
  endmoment timestamp with time zone NOT NULL,
  loc varchar(64) NOT NULL
);

CREATE TABLE people (
  id int PRIMARY KEY,
  fullname varchar(64) NOT NULL,
  age int NOT NULL,
  flex int NOT NULL,
  credit int NOT NULL
);

CREATE TABLE events_people (
  event_id int REFERENCES events,
  person_id int REFERENCES people
);

CREATE TABLE tags (
  id int PRIMARY KEY,
  iden varchar(32) NOT NULL
);

CREATE TABLE people_tags (
  tag_id int REFERENCES tags,
  person_id int REFERENCES people
);

CREATE TABLE events_tags (
  event_id int REFERENCES events,
  tag_id int REFERENCES tags
);
