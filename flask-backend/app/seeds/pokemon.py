from app.models import db, Pokemon, PokemonTypes
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
    "Bulbasaur",
    "Pidgeotto",
    "Pikachu",
    "Onyx",
    "Kingdra"
]

moves = [
    "Falcon Punch",
    "Throat Kick",
    "Flamethrower",
    "Water Gun",
    "Lightning",
    "Rock Slide",
    "Sandstorm",
    "Ice Beam"
]

def seed_pokemon():
    pokemons = [Pokemon(
        number=i,
        attack=randint(0, 100),
        defense=randint(0, 100),
        imageUrl=f"image{randint(0,100)}.png",
        name=names[i],
        type=choice(values),
        moves=moves[i]
    ) for i in range(0, 5)]

    for poke in pokemons:
        db.session.add(poke)
    db.session.commit()
    return pokemons

def undo_pokemon():
    db.session.execute(text("DELETE FROM Pokemons"))
    db.session.commit()
