from wtforms import StringField, SubmitField, IntegerField, FieldList
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL, Length

class CreatePokemon(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    attack = IntegerField("Attack", validators=[DataRequired()])
    defense = IntegerField("Defense", validators=[DataRequired()])
    imageUrl = StringField("Image URL", validators=[DataRequired(), URL(), Length(max=255)])
    type = StringField("Pokemon", validators=[DataRequired(), Length(max=255)])
    moves = FieldList(StringField('Name', validators=[DataRequired()]))
    submit = SubmitField("submit")
