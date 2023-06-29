from .pokemon import seed_pokemon, undo_pokemon
from .items import seed_items, undo_items

from flask.cli import AppGroup

seed_commands = AppGroup("seed")

@seed_commands.command("all")
def seed():
    pokemon = seed_pokemon()
    seed_items(pokemon)
    print('We are seeding our database')

@seed_commands.command("undo")
def undo():
    undo_items()
    undo_pokemon()
    print('We are destroying our data')
