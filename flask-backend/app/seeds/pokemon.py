from ..models import db, Pokemon
from sqlalchemy.sql import text
from random import randint, choice

values = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

names = [
    "Charmander",
    "Pikachu",
    "Farfetch'd",
    "Gengar",
    "Alakazam",
    "Squirtle",
    "Beedrill",
    "Dragonite",
    "Bulbasaur",
    "Hitmonlee",
    "Seal",
    "Pidgeotto",
    "Gastly",
    "Sandshrew",
    "Geodude",
    "Steelix"
]

moves = [
    "Flamethrower",
    "Thunderbolt",
    "Tackle",
    "Spite",
    "Psychic",
    "Water Gun",
    "Horn Drill",
    "Dragon Rage",
    "Vine Whip",
    "Falcon Punch",
    "Ice Beam",
    "Fly",
    "Poison",
    "Sandstorm",
    "Rock Slide",
    "Harden"
]

def seed_pokemon():
    pokemons = [Pokemon(
        number=i,
        attack=randint(0, 100),
        defense=randint(0, 100),
        imageUrl=f"image{randint(0,100)}.png",
        name=names[i],
        type=values[i],
        moves=moves[i]
    ) for i in range(len(values))]

    for poke in pokemons:
        db.session.add(poke)
    db.session.commit()
    return pokemons

def undo_pokemon():
    db.session.execute(text("DELETE FROM Pokemons"))
    db.session.commit()
