from db import db
from sqlalchemy.dialects.mysql import LONGTEXT
from models.category import Category

class Product(db.Model):
    __tablename__=' Product'

    productId = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(LONGTEXT)
    price = db.Column(db.Numeric(10,2))
    image = db.Column(db.String(256))
    categoryId = db.Column(db.String(128), db.ForeignKey(Category.categoryId))

    def __init__(self, productId, name, description, price, image, categoryId):
        self.productId = productId
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.categoryId = categoryId