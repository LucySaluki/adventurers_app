from flask import Blueprint, Flask, render_template, request, redirect
from models.place_types import PlaceType

import repositories.place_type_repository as place_type_repository

place_types_blueprint = Blueprint("place_types", __name__)

# INDEX
@place_types_blueprint.route("/place_types")
def place_types():
    place_types = place_type_repository.select_all()
    return render_template("place_types/index.html", place_types = place_types)

# NEW
@place_types_blueprint.route("/place_types/new")
def new_place_type():
    return render_template("place_types/new.html", place_types = place_types)


# CREATE
@place_types_blueprint.route("/place_types", methods=["POST"])
def create_place_type():
    type_name = request.form['type_name']
    new_place_type = PlaceType(type_name)
    place_type_repository.save(new_place_type)
    return redirect("/place_types")

# EDIT
@place_types_blueprint.route("/place_types/<id>/edit")
def edit_place_type(id):
    place_type = place_type_repository.select(id)
    return render_template('place_types/edit.html', place_type=place_type)

# UPDATE
@place_types_blueprint.route("/place_types/<id>", methods=["POST"])
def update_place_type(id):
    type_name = request.form["type_name"]
    new_place_type = PlaceType(type_name, id)
    place_type_repository.update(new_place_type)
    return redirect("/place_types")

# DELETE
@place_types_blueprint.route("/place_types/<id>/delete")
def delete_place_type(id):
    place_type_repository.delete(id)
    return redirect("/place_types")