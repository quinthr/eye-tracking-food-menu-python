from db import db
from sqlalchemy.dialects.mysql import LONGTEXT

class Category(db.Model):
    __tablename__=' Category'

    categoryId = db.Column(db.String(128), primary_key=True,)
    name = db.Column(db.String(128))
    description = db.Column(LONGTEXT)
    image = db.Column(db.String(256))
    products = db.relationship('Product', backref='category')

    def __init__(self, categoryId,name, description, image):
        self.categoryId = categoryId
        self.name = name
        self.description = description
        self.image = image