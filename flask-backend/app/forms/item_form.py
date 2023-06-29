from wtforms import Strinfield, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL, Length

class ItemForm(FlaskForm):
  happiness = Integerfield("Happiness", validators=[DataRequired()])
  imageUrl = Stringfield("imageUrl", validators=[DataRequired(), URL()])
  name = Stringfield("Name", validators=[DataRequired(), Length(max=255)])
  price = IntegerField("Price", validators=[DataRequired()])
  pokemonId = 
