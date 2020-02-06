from bl_web import db
from datetime import datetime

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
    image_url= db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"Inventory('{self.id}', '{self.inventory_id}','{self.part_num}', '{self.part_name}', '{self.part_type}', '{self.category_id}', '{self.color_id}', '{self.color_name}', '{self.quantity}', '{self.new_or_used}', '{self.unit_price}', '{self.description}', '{self.remarks}', '{self.is_stock_room}', '{self.image_url}', '{self.created_at}', '{self.updated_at}')"