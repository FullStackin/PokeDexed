from ..models import db, Item
from sqlalchemy.sql import text
from random import randint, choice

names = [
    "Potion",
    "Hi Potion",
    "Elixir",
    "Megalixir",
    "Rare Candy"
    "Pokeball",
    "Ultraball",
    "Moon Stone",
    "Quick Claw",
    "Moo Moo Milk",
    "Number Ten"
]

def seed_items(pokemons):
    items = [Item(
        happiness = randint(0, 10),
        imageUrl=f"image{randint(0,100)}.png",
        name=names[i],
        price=randint(100, 500),
        pokemon=choice(pokemons)
    ) for i in range(0, 10)]

    for item in items:
        db.session.add(item)

    db.session.commit()


def undo_items():
    db.session.execute(text("DELETE FROM Items"))
    db.session.commit()
