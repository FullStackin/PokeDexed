from flask import Blueprint
from app.models import Pokemon, PokemonTypes
from random import randint

pokemon = Blueprint("pokemon", __name__)


@pokemon.route('/')
def get_all_pokemon():
    pokemon = Pokemon.query.all()
    return pokemon

@pokemon.route('/types')
def get_pokemon_types():
    types = PokemonTypes.query.all()
    return types

@pokemon.route('/random')
def get_random_pokemon():
    pokemon = Pokemon.query.all()
    randomPokemon = pokemon[randint(0, len(pokemon))]
    return randomPokemon
