# create_db.py
from run import app
from taskmanager import db

with app.app_context():
    db.create_all()
    print("Database tables created.")
