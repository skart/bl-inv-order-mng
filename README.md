# BrickLink Seller Pages
Customized view of the Bricklink Seller functions without having to navigate the Bricklink website

### Inventory
Add, Update, and Delete inventory items. View Inventory by drawer.  

### Orders
Organized view, process and update orders.

## Setup
### Dependencies
Building and running the application requires the following:
- An installation of `Python 3`
- An installation of `pip` for `Python 3`
  - If it is not installed run `sudo apt-get install python3-pip`

### Repo Initial Setup
1. Clone this repository
2. Go to repository root directory
3. Run `pip3 install -r requirements.txt` to install all project dependencies

### Bricklink API
1. Go to bl_web directory
2. Copy `config.py.shadow` to `config.py` and fill out Bricklink API values
```bash
cp config.py.shadow config.py
vim config.py
```
### Database 
1. Go to bl_web directory
2. `python db_setup.py`
The script can take several minutes for to import a large inventory

## To Do
### Inventory
* Logic for update that includes a new color => get new image
* Update on page for drawers
* Update on page for item
* Button to sync BL to DB
* Sort Inventory by Category 

### Orders
* Orders on the homepage
* Order page
* Update processed order
* Update shipped order
* Query USPS shipping for delivered status??
* More order stuff...

### Overall
* Nicer theme

#### Maybe...
* Auto search fields on Inventory page (dynamically update as chars are typed)

