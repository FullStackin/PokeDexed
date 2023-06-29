from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL, Length

class EditItemForm(FlaskForm):
  happiness = IntegerField("Happiness", validators=[DataRequired()])
  imageUrl = StringField("imageUrl", validators=[DataRequired(), URL()])
  name = StringField("Name", validators=[DataRequired(), Length(max=255)])
  price = IntegerField("Price", validators=[DataRequired()])
  pokemonId = IntegerField("Pokemon", validators=[DataRequired()])
  submit = SubmitField("submit")
