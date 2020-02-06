from helpers.bricklink import ApiClient
from config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath('..'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, nullable=False)
    part_num = db.Column(db.Integer, nullable=False)
    part_name = db.Column(db.String(60), nullable=False)
    part_type = db.Column(db.String(15), nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    color_id = db.Column(db.Integer, nullable=False)
    color_name = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    new_or_used = db.Column(db.String(1), nullable=False)
    unit_price = db.Column(db.Float, nullable=False, default=0.01)
    description = db.Column(db.Text)
    remarks = db.Column(db.String(20), nullable=False)
    is_stock_room = db.Column(db.Boolean, nullable=False, default=False)
    image_url = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"Inventory('{self.id}', '{self.inventory_id}','{self.part_num}', '{self.part_name}', '{self.part_type}', '{self.category_id}', '{self.color_id}', '{self.color_name}', '{self.quantity}', '{self.new_or_used}', '{self.unit_price}', '{self.description}', '{self.remarks}', '{self.is_stock_room}', '{self.image_url}', '{self.created_at}', '{self.updated_at}')"

db.create_all()

# make api call, capture response
client = ApiClient()
response = client.get('inventories')

# convert API reponse to database format
for x in response["data"]:
    # get img url
    img_response = client.get(
        "items/{}/{}/images/{}".format(x["item"]["type"], x["item"]["no"], x["color_id"]))
    try:
        img_url = img_response["data"]["thumbnail_url"]
    except Exception as e:
        img_url = ""
    # create record to add
    record = Inventory(inventory_id=x["inventory_id"], part_num=x["item"]["no"], part_name=x["item"]["name"], part_type=x["item"]["type"], category_id=x["item"]["category_id"], color_id=x["color_id"],
                       color_name=x["color_name"], quantity=x["quantity"], new_or_used=x["new_or_used"], unit_price=x["unit_price"], description=x["description"], remarks=x["remarks"], is_stock_room=x["is_stock_room"], image_url=img_url)
    db.session.add(record)
    db.session.commit()
