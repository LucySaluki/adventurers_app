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
    sql = "DELETE FROM places"
    run_sql(sql)

# select all
def select_all():
    places = []
    sql = "SELECT * FROM places"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["id"])
        place=Place(row['place_name'],row['description'],row['place_type'],country,row['visited'],row['id'])
        places.append(place)
    return places

# select individual
def select(id):
    plsce = None
    sql = "SELECT * FROM places where id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        place = Place(result['place_name'],result['description'],result['place_type'],country,result['visited'],result['id'])
    return place

# delete individual

# update individual
