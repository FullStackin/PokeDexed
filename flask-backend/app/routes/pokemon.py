from flask import Blueprint, jsonify
from app.models import Pokemon, PokemonTypes
from random import randint
import json


pokemon = Blueprint("pokemon", __name__)

@pokemon.route('/')
def get_all_pokemon():
    data = Pokemon.query.all()
    print(data)
    pokemon = [key.to_dict() for key in data]
    return pokemon

@pokemon.route('/types')
def get_pokemon_types():
    # data = PokemonTypes.query.all()
    # print(data)
    # types = [key.to_dict() for key in data]
    return [
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
        "steel"
    ]

@pokemon.route('/random')
def get_random_pokemon():
    pokemon = Pokemon.query.all()
    randomPokemon = pokemon[randint(0, len(pokemon) - 1)]
    data = randomPokemon.to_dict()
    return data

@pokemon.route('/<int:id>')
def get_single_pokemon(id):
    pokemon = Pokemon.query.get(id)
    list_moves = pokemon.moves.split(',')
    data = pokemon.to_dict();
    type = str(pokemon.type)
    data["moves"] = list_moves
    data["type"] = type.split('.')[1]
    data["attack"] = pokemon.attack
    data["defense"] = pokemon.defense
    data["createdAt"] = pokemon.createdAt
    data["updatedAt"] = pokemon.updatedAt
    return data


@pokemon.route('/', methods=['POST'])
def create_pokemon():
    form = CreateForm()
    new_pokemon = Pokemon(
        number=form.data["number"],
        attack=form.data["attack"],
        defense=form.data["defense"],
        imageUrl=form.data["imageUrl"],
        name=form.data["name"],
        type=form.data["type"],
        moves=form.data["moves"]
    )
    db.session.add(new_pokemon)
    db.session.commit()
