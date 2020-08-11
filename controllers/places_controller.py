from flask import Blueprint, Flask, render_template, request, redirect
from models.places import Place

import repositories.place_repository as place_repository
import repositories.place_type_repository as place_type_repository
import repositories.country_repository as country_repository

places_blueprint = Blueprint("places", __name__)
countries_blueprint =Blueprint("countries", __name__)

# INDEX
# create a place object and fill with all places using the repository
# open the main places page using that object to populate the fields
@places_blueprint.route("/places")
def places():
    places = place_repository.select_all()
    return render_template("places/index.html", places = places)

# NEW
# open a new blank places page
@places_blueprint.route("/places/new")
def new_place():
    countries =country_repository.select_all()
    place_types =place_type_repository.select_all()
    return render_template("places/new.html", countries=countries, place_types = place_types)


# CREATE
# from the new placess input get each of the field values
# create a new place object
# return to the places page to show the new entry
@places_blueprint.route("/places", methods=["POST"])
def create_place():
    place_name = request.form['place_name']
    description=request.form['description']
    place_type_id = request.form['place_type_id']
    place_type = place_type_repository.select(place_type_id)
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    visited = request.form['visited']
    rating=request.form['rating']
    new_place = Place(place_name,description, place_type, country, visited,rating)
    place_repository.save(new_place)
    return redirect("/places")

#SHOW DETAILS FILTERED
# select all the places based on the visited criteria true of false from the page address
# go to the places show page based and display the places objects
@places_blueprint.route("/places/<visited>/show")
def show_place_filtered(visited):
    places = place_repository.select_filtered(visited)
    return render_template('places/show.html', places=places)

# SEARCH CRITERIA
# get the continent value from the dropdown
# go to the continent page
@places_blueprint.route("/places/criteria", methods=['POST'])
def search_criteria():
    continent=request.form['continent']
    return redirect(f"/places/{continent}")

#SHOW DETAILS FROM SEARCH
# using the continent value from the page select all the countries on that continient
# go to the output search page using the list of places created and the continent name
@places_blueprint.route("/places/<continent>")
def show_place_search(continent):
    places = place_repository.select_search(continent)
    return render_template('places/search.html', places=places, continent=continent)

# EDIT
# use the id to select a specific place
# return that entry in editing mode and pre-populated
@places_blueprint.route("/places/<id>/edit")
def edit_place(id):
    countries =country_repository.select_all()
    place_types =place_type_repository.select_all()
    place = place_repository.select(id)
    return render_template('places/edit.html', place_types=place_types, countries=countries, place=place)

# UPDATE
# from the place edit input get each of the field values
# create a new place, setting the id to the exisiting id
# use that new place to update the existing item via the id
# return to the places page to show the edited entry
@places_blueprint.route("/places/<id>", methods=["POST"])
def update_place(id):
    place_name = request.form["place_name"]
    description=request.form['description']
    place_type_id = request.form["place_type_id"]
    place_type = place_type_repository.select(place_type_id)
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    visited = request.form["visited"]
    rating = request.form["rating"]
    new_place = Place(place_name,description, place_type, country, visited,rating,id)
    place_repository.update(new_place)
    return redirect("/places")

# DELETE
# select a specific place by id 
# use the repository delete to remove the entry 
# return to main places page
@places_blueprint.route("/places/<id>/delete")
def delete_place(id):
    place_repository.delete(id)
    return redirect("/places")
