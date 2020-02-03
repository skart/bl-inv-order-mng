# Create Inventory Table

import sqlite3
import sys, os
sys.path.append(os.path.abspath('..'))
from config import *

# connection to db
conn = sqlite3.connect(ROOT_DIR+'/site.db')

# create Inventory table
conn.execute('''CREATE TABLE Inventory
         (ID INT PRIMARY KEY NOT NULL,
         INVENTORY_ID INT NOT NULL,
         PART_NUM INT NOT NULL,
         PART_NAME CHAR(60) NOT NULL,
         PART_TYPE CHAR(15) NOT NULL,
         CATEGORY_ID INT NOT NULL,
         COLOR_ID INT NOT NULL,
         COLOR_NAME CHAR(30) NOT NULL,
         QUANTITY INT NOT NULL,
         NEW_OR_USED CHAR(1) NOT NULL,
         UNIT_PRICE REAL NOT NULL,
         DESCRIPTION CHAR(60),
         REMARKS CHAR(20) NOT NULL,
         IS_STOCK_ROOM BOOLEAN NOT NULL);''')

# close db connection
conn.close()