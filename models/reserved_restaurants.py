from db import db


class ReservedRestaurantModel(db.Model):
    __tablename__ = "reserved_restaurants"

    id = db.Column(db.Integer, primary_key=True)
    businessId = db.Column(db.String(22), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.Text(), nullable=False)
    yelp_url = db.Column(db.Text(), nullable=False)

    people = db.Column(db.Integer, nullable=False)
    dt = db.Column(db.DateTime, nullable=False)