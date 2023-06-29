from flask import Blueprint, request, jsonify
from ..models import db, Item
from app.forms.item_form import EditItemForm


item = Blueprint("item", __name__)

@item.route('/<int:id>', methods = ["POST"])
def edit_item(id):
  item = Item.query.get(id)
  # print("item   ", item)
  form = EditItemForm()
  # data = request.get_json()
  form['csrf_token'].data = request.cookies['csrf_token']
  # print(form.data)
  # print(item.name)
  # print(form.data["name"])
  item.name = form.data["name"]
  item.imageUrl = form.data["imageUrl"]
  item.happiness = form.data["happiness"]
  item.price = form.data["price"]
  db.session.commit()


  # print("form data")
  # print("item    ", item)
  # print("blahblah  ", request.data)
  # return {"msg": "blah"}
  return request.get_json()


#works w/o specifying method =["DELETE"]
@item.route('/<int:id>')
def delete_item(id):
  item = Item.query.get(id)
  if not item:
    return {"message":"item not found"}
  db.session.delete(item)
  db.session.commit()
  return { "id": id}
