from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ReservedRestaurantSchema
from models import ReservedRestaurantModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("ReservedRestaurant", "reserved_restaurants",
                description="Operations to reserve and retrieve reservations")


@blp.route("/reserve")
class ReservedRestaurant(MethodView):
    @blp.arguments(ReservedRestaurantSchema)
    def post(self, restaurant_data):
        reserved_restaurant = ReservedRestaurantModel(**restaurant_data)

        try:
            db.session.add(reserved_restaurant)
            db.session.commit()

        except IntegrityError:
            abort(400, message="A reservation with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating a reservation.")

        return {"message": "A reservation has been created."}, 201

    @blp.response(200, ReservedRestaurantSchema(many=True))
    def get(self):
        return ReservedRestaurantModel.query.all()
