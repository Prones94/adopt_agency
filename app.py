from flask import Flask, render_template, redirect, request, flash

from forms import AddPetForm, EditPetForm
from models import db,connect_db, Pet


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'adoptapet1'

# Initialize the database
connect_db(app)
db.create_all()


@app.route('/')
def home_page():
  """Home Page listing available and not available pets"""
  # Query for available and unavailable pets
  available_pets = Pet.query.filter_by(available=True).all()
  unavailable_pets = Pet.query.filter_by(available=False).all()
  return render_template("homepage.html", available_pets=available_pets, unavailable_pets=unavailable_pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_form():
  """Shows form to add new pet and also handles form submission"""
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

    flash(f"Added {new_pet.name}!", "success")
    return redirect('/')
  else:
    return render_template('add_pet.html',form=form)

@app.route('/<int:pet_id>', methods=["GET","POST"])
def show_edit_pet_form(pet_id):
  """Shows pet details and can edit its details"""
  pet = Pet.query.get_or_404(pet_id)
  form = EditPetForm(obj=pet)

  if form.validate_on_submit():
    pet.photo = form.photo.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.commit()
    flash(f"Updated {pet.name}!")
    return redirect('/')
  else:
    return render_template('pet_detail.html', form=form, pet=pet)


if __name__ == '__main__':
  app.run(debug=True)
