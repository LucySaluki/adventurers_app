from flask import Blueprint, Flask, render_template

from models.countries import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)