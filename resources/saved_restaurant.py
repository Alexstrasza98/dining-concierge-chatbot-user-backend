import json

from flask import Response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SavedRestaurantSchema
from models import SavedRestaurantModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("SavedRestaurant", "saved_restaurants", description="Operations to save and retrieve restaurants")


@blp.route("/save")
class SavedRestaurant(MethodView):
    @blp.arguments(SavedRestaurantSchema)
    def post(self, restaurant_data):
        saved_restaurant = SavedRestaurantModel(**restaurant_data)

        try:
            db.session.add(saved_restaurant)
            db.session.commit()

        except IntegrityError:
            abort(400, message="A restaurant with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating a restaurant.")

        return {"message": "A restaurant has been saved."}, 201

    @blp.response(200, SavedRestaurantSchema(many=True))
    def get(self):
        data = SavedRestaurantModel.query.all()
        response = blp.response_class(
            response=json.dumps(data),
            mimetype="application/json"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
