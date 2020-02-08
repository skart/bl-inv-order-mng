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
* Update Item in Drawer
** Send update to Bricklink
* Delete item in drawer
** Send delete to Bricklink
* Add new item
** Error validation
** Send add to Bricklink
* Orders on the homepage
* Order page
* More oder stuff

#### Maybe...
* Part Search with inventory results

