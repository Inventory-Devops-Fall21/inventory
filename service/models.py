"""
Models for the Inventory Service

All of the models are stored in this module

Models
------
Inventory - An Inventory used keep track of products

Attributes:
-----------
name (string) - the name of the product
quantity (int) - the quantity of the product

"""
import logging
from enum import Enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from service import keys

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()

def init_db(app):
    """Initialies the SQLAlchemy app"""
    Inventory.init_db(app)

class DataValidationError(Exception):
    """ Used for an data validation errors when deserializing """

    pass

class Inventory(db.Model):
    
    app:Flask = None
    
    # Inventory Schema //id
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(100)) #[old, new, used]
    quantity = db.Column(db.Integer)
    restock_level = db.Column(db.Integer)
    
    ##################################################
    # INSTANCE METHODS
    ##################################################
    
    def __repr__(self):
        return "<id=%r name=%s quantity=%s>" % (self.id, self.name, self.quantity)
    
    def create(self):
        """
        Creates a Inventory to the database
        """
        logger.info("Creating %s", self.name)
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """
        Updates an Inventory to the database
        """
        logger.info("Updating %s", self.name)
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """
        Removes a product from the data store"""
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """ Serializes an Inventory record into a dictionary """
        return {
            keys.KEY_NAME: self.name,
            keys.KEY_PID: self.id,
            keys.KEY_QTY: self.quantity,
            keys.KEY_LVL: self.restock_level,
            keys.KEY_CND: self.condition,
        }

    
    def deserialize(self, data):
        """ 
        Deserializes a Inventory from a dictionary 
        Args:
            data (dict): A dictionary containing the Inventory data
        """
        try:
            self.name = data[keys.KEY_NAME]
            self.id = data[keys.KEY_PID]
            self.quantity = data[keys.KEY_QTY]
            self.restock_level = data[keys.KEY_LVL]
            self.condition = data[keys.KEY_CND]
            return self
        except KeyError as error:
            raise DataValidationError("Invalid Inventory record: missing " + error.args[0])
        except TypeError as error:
            raise DataValidationError("Invalid Inventory record: body contained bad or no data")

    ##################################################
    # CLASS METHODS
    ##################################################

    @classmethod
    def init_db(cls, app:Flask):
        """Initializes the database session

        :param app: the Flask app
        :type data: Flask

        """
        logger.info("Initializing database")
        cls.app = app
        # This is where we initialize SQLAlchemy from the Flask app
        db.init_app(app)
        app.app_context().push()
        db.create_all()  # make our sqlalchemy tables
    
    @classmethod
    def find_all(cls) -> list:
        """Returns all of the Inventory in the database"""
        logger.info("Processing all Inventory")
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id:int):
        """Find an Inventory by it's id

        :param id: the id of the Inventory to find
        :type id: int

        :return: an instance with the id, or None if not found
        :rtype: Inventory

        """
        logger.info("Processing lookup for id %s ...", id)
        return cls.query.get(id)
