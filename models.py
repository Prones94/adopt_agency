from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class Pet(db.Model):
  """Pet Models"""
  __tablename__ = "pets"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False, unique=True)
  species = db.Column(db.Text, nullable=False)
  photo = db.Column(db.Text, nullable=True)
  age = db.Column(db.Integer, nullable=True)
  notes = db.Column(db.Text, nullable=True)
  available = db.Column(db.Boolean, nullable=False, default=True)
