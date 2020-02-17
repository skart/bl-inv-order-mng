from flask import render_template, url_for, flash, redirect, request, abort
from bl_web import app, db
from bl_web.models import Inventory, Colors
from bl_web.forms import InvForm
from bl_web.bricklink import ApiClient

client = ApiClient()

@app.route('/')
@app.route("/home")
def home():
    query = Inventory.query.group_by(Inventory.remarks)
    return render_template('home.html', drawers=query)

@app.route('/drawer/<drawer_name>')
def show_drawer(drawer_name):
    query = Inventory.query.filter_by(remarks=drawer_name).all()
    return render_template('drawer.html', drawer_name=drawer_name, inv=query)

@app.route('/inventory')
def inventory():
    query = Inventory.query.all()
    return render_template('inventory.html', inv=query)

@app.route("/inventory/new", methods=['GET', 'POST'])
def new_item():
    form = InvForm()
    form.color_name.choices = [(a.color_id, a.color_name) for a in Colors.query.order_by(Colors.color_name)]
    if form.validate_on_submit():
        # format to json params
        data = {
			'item': {'no': form.part_num.data, 'type': form.part_type.data},
			'quantity': form.quantity.data,
        	'unit_price': form.unit_price.data,
        	'new_or_used': form.new_or_used.data,
        	'color_id': form.color_name.data,
        	'description': form.description.data,
        	'remarks': form.remarks.data,
        	'bulk': 1,
        	'is_retain': False,
        	'is_stock_room': form.is_stock_room.data,
        }

        response = client.post("inventories", data)

        img_response = client.get("items/{}/{}/images/{}".format(response["data"]["item"]["type"], response["data"]["item"]["no"], response["data"]["color_id"]))
        try:
        	img_url = img_response["data"]["thumbnail_url"]
        except Exception as e:
        	img_url = ""
        color = Colors.query.filter_by(color_id=form.color_name.data).first()
        record = Inventory(
        				inventory_id=response["data"]["inventory_id"],
    					part_num=response["data"]["item"]["no"], 
    					part_name=response["data"]["item"]["name"],
    					part_type=response["data"]["item"]["type"], 
    					category_id=response["data"]["item"]["category_id"], 
    					color_id=response["data"]["color_id"],
                       	color_name=color.color_name, ###### need to return color name.
                       	quantity=response["data"]["quantity"], 
                       	new_or_used=response["data"]["new_or_used"], 
                       	unit_price=response["data"]["unit_price"], 
                       	description=response["data"]["description"], 
                       	remarks=response["data"]["remarks"], 
                       	is_stock_room=response["data"]["is_stock_room"], 
                       	image_url=img_url
                       	)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_item.html', form=form)

@app.route("/inventory/<int:inv_id>")
def inv_item(inv_id):
    item = Inventory.query.get_or_404(inv_id)
    return render_template('item.html', item=item)

@app.route("/inventory/<int:inv_id>/update", methods=['GET', 'POST']) 
def update_item(inv_id):
    item = Inventory.query.get_or_404(inv_id)
    form = InvForm()
    form.color_name.choices = [(a.color_id, a.color_name) for a in Colors.query.order_by(Colors.color_name)]
    if form.validate_on_submit():
        # format to json params
        quantity_adjust = int(form.quantity.data) - int(item.quantity)
        # if quantity < 0:
        # 	str(quantity_adjust)
        data = { 
			'item': {'no': form.part_num.data, 'type': form.part_type.data},
			'quantity': quantity_adjust,
        	'unit_price': form.unit_price.data,
        	'new_or_used': form.new_or_used.data,
        	'color_id': form.color_name.data,
        	'description': form.description.data,
        	'remarks': form.remarks.data,
        	'bulk': 1,
        	'is_retain': False,
        	'is_stock_room': form.is_stock_room.data,
        }
        response = client.put("inventories/{}".format(item.inventory_id), data)
        color_query = Colors.query.filter_by(color_id=form.color_name.data).first()
        app.logger.info(color_query)
        item.part_num = form.part_num.data
        item.part_type = form.part_type.data
        item.color_name = color_query.color_name
        item.quantity = form.quantity.data
        item.new_or_used = form.new_or_used.data
        item.unit_price = form.unit_price.data
        item.description = form.description.data
        item.remarks = form.remarks.data
        item.is_stock_room = form.is_stock_room.data
        db.session.commit()
        flash('Item has been updated!', 'success')
        return redirect(url_for('inv_item', inv_id=item.id))
    elif request.method == 'GET':
    	form.part_num.data = item.part_num
    	form.part_type.data = item.part_type
    	form.color_name.data = item.color_name
    	form.quantity.data = item.quantity
    	form.new_or_used.data = item.new_or_used
    	form.unit_price.data = item.unit_price
    	form.description.data = item.description
    	form.remarks.data = item.remarks
    	form.is_stock_room.data = item.is_stock_room
    return render_template('new_item.html', form=form)

@app.route("/inventory/<int:inv_id>/delete", methods=['POST'])
def delete_item(inv_id):
    item = Inventory.query.get_or_404(inv_id)
    client.delete("inventories/{}".format(item.inventory_id))
    db.session.delete(item)
    db.session.commit()
    flash('The item has been deleted!', 'success')
    return redirect(url_for('home'))