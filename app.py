from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Initialize the database
connect_db(app)
db.create_all()

# Initialize debug toolbar
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
  """Home Page lists pets name, photo, and availability"""
  pets = Pet.query.all()
  return render_template("homepage.html", pets=pets)