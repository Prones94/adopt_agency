from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm
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

@app.route('/add', methods=["GET", "POST"])
def add_pet():
  """Form to add a new pet"""
  form = AddPetForm()
  if form.validate_on_submit():
    new_pet = Pet(
      name = form.name.data,
      species = form.species.data,
      photo = form.photo.data,
      age = form.age.data,
      notes = form.notes.data,
      available=True
      )
    db.session.add(new_pet)
    db.session.commit()

    return redirect('/')
  else:
    return render_template('add_pet.html',form=form)