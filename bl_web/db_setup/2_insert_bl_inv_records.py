# Add Bricklink Inventory to Inventory Table

import sqlite3
import sys, os, json
sys.path.append(os.path.abspath('..'))
from config import *
from helpers.bricklink import ApiClient

# connection to db
conn = sqlite3.connect(ROOT_DIR+'/site.db')

# make api call, capture response
client = BLClient()
response = client.get('inventories')
items = []
main_id = 0

# convert API reponse to database format
for x in response["data"]:
	main_id += 1
	items.append([\
            main_id,\
            x["inventory_id"],\
            x["item"]["no"],\
            x["item"]["name"],\
            x["item"]["type"],\
            x["item"]["category_id"],\
            x["color_id"],\
            x["color_name"],\
			x["quantity"],\
			x["new_or_used"],\
			x["unit_price"],\
			x["description"],\
			x["remarks"],\
			x["is_stock_room"]
    ])

# insert the items into the Inventory table    
conn.executemany("INSERT INTO Inventory VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", items)

# commit records
conn.commit()

# close db connection
conn.close()