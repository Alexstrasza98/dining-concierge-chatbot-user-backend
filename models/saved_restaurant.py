from db import db


class SavedRestaurantModel(db.Model):
    __tablename__ = "saved_restaurants"

    id = db.Column(db.Integer, primary_key=True)
    businessId = db.Column(db.String(22), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    rate = db.Column(db.Float(), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(10))
    image_url = db.Column(db.Text(), nullable=False)
    yelp_url = db.Column(db.Text(), nullable=False)
