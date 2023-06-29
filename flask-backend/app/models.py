from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class MyEnum(Enum):
    pass

# [
#   "fire",
#   "electric",
#   "normal",
#   "ghost",
#   "psychic",
#   "water",
#   "bug",
#   "dragon",
#   "grass",
#   "fighting",
#   "ice",
#   "flying",
#   "poison",
#   "ground",
#   "rock",
#   "steel",
# ]

class Pokemon(db.Model):
    __tablename__ = "Pokemons"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum)

class PokeMonType(db.Model):
    pass

class Item(db.Model):
    pass
