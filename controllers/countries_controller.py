from flask import Blueprint, Flask, render_template, request, redirect

from models.countries import Country
import repositories.country_repository as country_repository
import repositories.place_repository as place_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
# create a countries object and fill with all countries using the repository
# open the main countries page using that object to populate the fields
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)

# NEW
# open a new blank countries page
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html")


# CREATE
# from the new countries input get each of the field values
# create a new country setting the visited to false in the first instance
# return to the countries page to show the new entry
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    continent=request.form['continent']
    new_country = Country(name,continent,False)
    country_repository.save(new_country)
    return redirect("/countries")


# EDIT
# use the id to select a specific country
# return that entry in editing mode and pre-populated
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country=country)


# UPDATE
# from the country edit input get each of the field values
# create a new country, setting the id to the exisiting id
# use that new country to update the existing item via the id
# return to the countries page to show the edited entry
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    continent = request.form["continent"]
    country_visited = country_repository.select(id)
    country = Country(name, continent, country_visited.visited, id)
    country_repository.update(country)
    return redirect("/countries")


# DELETE
# select a specific country by id 
# use the repository delete to remove the entry 
# return to main countries page
@countries_blueprint.route("/countries/<id>/delete")
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")
