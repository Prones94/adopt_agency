from optparse import Option
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
  """Form for adding pets"""
  name = StringField("Pet Name", validators=[InputRequired()])
  species = StringField("Pet Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'fish','lizard', 'bird'], message="Species must be cat, dog, fish, lizard, or bird")])
  photo = StringField("Photo URL", validators=[Optional(),URL()])
  age = IntegerField("Age of Pet", validators=[Optional(), NumberRange(min=0,max=30,message="Age of pet must be between 0 and 30")])
  notes = StringField("Pet Details", validators=[Optional()])