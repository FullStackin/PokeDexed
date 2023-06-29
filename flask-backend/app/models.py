from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from datetime import datetime

db = SQLAlchemy()

class PokemonTypes(Enum):
    fire = "fire"
    electric = "electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water = "water"
    bug = "bug"
    dragon = "dragon"
    grass = "grass"
    fighting = "fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock = "rock"
    steel = "steel"


class Pokemon(db.Model):
    __tablename__ = "Pokemons"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum(PokemonTypes), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Float(3,2), default=1.00, nullable=False)
    catchRate = db.Column(db.Float(3,2), default=1.00, nullable=False)
    captured = db.Column(db.Boolean, default=False, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now() )
    updatedAt = db.Column(db.DateTime, default=datetime.now() )

    items = db.relationship("Item", back_populates="pokemon")

class Item(db.Model):
    __tablename__ = 'Items'

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey('Pokemons.id'))
    createdAt = db.Column(db.DateTime, default=datetime.now() )
    updatedAt = db.Column(db.DateTime, default=datetime.now() )

    pokemon = db.relationship("Pokemon", back_populates="items")
