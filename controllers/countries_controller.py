from flask import Blueprint, Flask, render_template, request, redirect

from models.countries import Country
import repositories.country_repository as country_repository

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
    new_country = Country(name)
    country_repository.save(new_country)
    return redirect("/countries")