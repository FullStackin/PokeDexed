from flask import Blueprint, request
from ..models import db, Item
from app.forms.item_form import EditItemForm


item = Blueprint("item", __name__)

@item.route('/<int:id>', methods = ["PUT"])
def edit_item(id):
  form = EditItemForm()

  form['csrf_token'].data = request.cookies['csrf_token']
  # form["name"].data = request.form["name"]
  item = Item.query.get(id)
  print("form data   ", form.data)
  print("item    ", item)
  print("blahblah  ", request.data)
  return {"msg": "received"}


#works w/o specifying method =["DELETE"]
@item.route('/<int:id>')
def delete_item(id):
  item = Item.query.get(id)
  if not item:
    return {"message":"item not found"}
  db.session.delete(item)
  db.session.commit()
  return { "id": id}
