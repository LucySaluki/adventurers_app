from flask import Blueprint, Flask, render_template, request, redirect
from models.places import Place

import repositories.place_repository as place_repository
import repositories.country_repository as country_repository

places_blueprint = Blueprint("places", __name__)
countries_blueprint =Blueprint("countries", __name__)

# INDEX
@places_blueprint.route("/places")
def places():
    places = place_repository.select_all()
    return render_template("places/index.html", places = places)

# NEW
@places_blueprint.route("/places/new")
def new_place():
    return render_template("places/new.html")


# CREATE
@places_blueprint.route("/places", methods=["POST"])
def create_place():
    place_name = request.form["place_name"]
    description=request.form['description']
    place_type = request.form["place_type"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    visited = request.form["visited"]
    new_place = Place(place_name,description, place_type, country, visited)
    place_repository.save(new_place)
    return redirect("/places")

#SHOW DETAILS
@places_blueprint.route("/placess/<id>")
def edit_places(id):
    place = place_repository.select(id)
    return render_template('places/edit.html', place=place)

# EDIT
@places_blueprint.route("/places/<id>/edit")
def edit_place(id):
    place = place_repository.select(id)
    return render_template('places/edit.html', place=place)

# UPDATE
@places_blueprint.route("/places/<id>", methods=["POST"])
def update_place(id):
    place_name = request.form["place_name"]
    description=request.form['description']
    place_type = request.form["place_type"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    visited = request.form["visited"]
    new_place = Place(place_name,description, place_type, country, visited)
    place_repository.update(new_place)
    return redirect("/places")

# DELETE
@places_blueprint.route("/[places/<id>/delete")
def delete_place(id):
    place_repository.delete(id)
    return redirect("/places")
