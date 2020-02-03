from flask import Flask, render_template
from bl_web import app
from bl_web.models import Inventory

@app.route('/')
def homepage():
    query = Inventory.query.group_by(Inventory.remarks)
    return render_template('home.html', drawers=query)

@app.route('/inventory')
def inventory():
    query = Inventory.query.all()
    return render_template('inventory.html', inv=query)

@app.route('/drawer/<drawer_name>')
def show_drawer(drawer_name):
    query = Inventory.query.filter_by(remarks=drawer_name).all()
    return render_template('drawer.html', drawer_name=drawer_name, inv=query)