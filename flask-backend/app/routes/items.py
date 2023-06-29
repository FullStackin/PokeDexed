from flask import Blueprint
from ..models import db, Item


item = Blueprint("item", __name__)

@item.route('/<int:id>')
def edit_item(id):


@item.route('/<int:id>')
def delete_item(id):
  item = Item.query.get(id)
  if not item:
    return {"message":"item not found"}
  db.session.delete(item)
  db.session.commit()
  return { "id": id}
