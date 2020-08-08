from flask import Blueprint, Flask, render_template
from models.places import Place

import repositories.place_repository as place_repository
import repositories.country_repository as country_repository

places_blueprint = Blueprint("places", __name__)

# INDEX
@places_blueprint.route("/places")
def places():
    places = place_repository.select_all()
    return render_template("places/index.html", places = places)