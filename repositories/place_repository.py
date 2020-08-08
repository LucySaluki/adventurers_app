from db.run_sql import run_sql
from models.places import Place
from models.countries import Country

import repositories.country_repository as country_repository

# save
def save(place):
    sql = "INSERT INTO places (place_name, description, place_type, country_id, visited) VALUES (%s, %s, %s,%s, %s) RETURNING id"
    values =[place.place_name, place.description, place.place_type, place.country.id, place.visited]
    result = run_sql(sql,values)[0]
    place.id = result['id']
    return place

# delete all
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

# select all

# select individual

# delete individual

# update individual
