"""
The generic variables for ALL the programs
"""

# __init__.py
DATABASE_URI_LOCAL = "postgres://postgres:postgres@localhost:5432/postgres"

# service.py
DEMO_MSG = "Inventory REST API Service"

# routes.py
KEY_NAME='name'
KEY_PID='id'
KEY_CND='condition'
KEY_QTY='quantity'
KEY_LVL='restock_level'
KEY_AVL='available'
KEY_CONTENT_TYPE_JSON="application/json"

# model.py
CONDITIONS = ["new", "used", "open box"]
AVAILABLE_TRUE = 1
AVAILABLE_FALSE = 0
QTY_LOW = 0
QTY_HIGH = 50
QTY_STEP = 1
RESTOCK_LVL = 50
MAX_ATTR = 5

ATTR_DEFAULT = 0
ATTR_id = 1
ATTR_CONDITION = 2
ATTR_QUANTITY = 3
ATTR_RESTOCK_LEVEL = 4
ATTR_AVAILABLE = 5
