from app.models import db, Pokemon
from app import app
from app.models import PokemonTypes, Item

with app.app_context():
    # db.drop_all()
    # print("All tables dropped!")
    # db.create_all()
    # print("Created all tables!")

    poke = Pokemon(
        number = 6,
        attack = 5,
        defense = 3,
        imageUrl = "www.google.com/pic.png",
        name = "roman",
        type = PokemonTypes.fire,
        moves = "falcon_kick,throat_punch"
    )
    db.session.add(poke)
    db.session.commit()
    print(poke)

    item = Item(
        happiness = 5,
        imageUrl = "lalala.png",
        name = "jonathan",
        price = 3,
    )
    poke.items.append(item)
    db.session.add(item)
    db.session.commit()
    print("foreign key value --- ", item.pokemonId)
    print("poke's item ---   ", poke.items)

    # poke2 = Pokemon(
    #     number = 66,
    #     attack = 5,
    #     defense = 3,
    #     imageUrl = "www.google.com/pic.png",
    #     name = "jonathan",
    #     type = "roman",

    # )
    # db.session.add(poke2)
    # db.session.commit()
    # print(poke2.type)
