from flask import Blueprint, Flask, render_template, request, redirect

from models.countries import Country
import repositories.country_repository as country_repository
import repositories.place_repository as place_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)

# NEW
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html")


# CREATE
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    continent=request.form['continent']
    new_country = Country(name,continent,False)
    country_repository.save(new_country)
    return redirect("/countries")


# EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country=country)


# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    continent = request.form["continent"]
    country = Country(name, continent, id)
    country_repository.update(country)
    return redirect("/countries")


# DELETE
@countries_blueprint.route("/countries/<id>/delete")
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")
