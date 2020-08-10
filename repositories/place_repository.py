from db.run_sql import run_sql
from models.places import Place
from models.countries import Country
from models.place_types import PlaceType

import repositories.country_repository as country_repository
import repositories.place_type_repository as place_type_repository

# save
def save(place):
    sql = "INSERT INTO places (place_name, description, place_type_id, country_id, visited, rating) VALUES (%s, %s, %s,%s, %s, %s) RETURNING id"
    print(place.visited)
    values =[place.place_name, place.description, place.place_type.id, place.country.id, place.visited, place.rating]
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
    sql = "SELECT places.* FROM places inner join countries on places.country_id = countries.id order by countries.name, places.place_name"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["country_id"])
        place_type = place_type_repository.select(row["place_type_id"])
        place=Place(row['place_name'],row['description'],place_type,country,row['visited'],row['rating'], row['id'])
        places.append(place)
    return places

# select individual
def select(id):
    place = None
    sql = "SELECT * FROM places where id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        place_type = place_type_repository.select(result['place_type_id'])
        place=Place(result['place_name'],result['description'],place_type,country,result['visited'],result['rating'], result['id'])
    return place

# delete individual
def delete(id):
    sql = "DELETE FROM places WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
def update(place):
    sql = "UPDATE places SET (place_name, description, place_type_id, country_id, visited, rating) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [place.place_name, place.description, place.place_type.id, place.country.id, place.visited, place.rating, place.id]
    run_sql(sql, values)

# select individual filtered
def select_filtered(visited):
    places = []
    sql = "SELECT * FROM places where visited = %s"
    values = [visited]
    results = run_sql(sql,values)

    for row in results:
        country = country_repository.select(row['country_id'])
        place_type = place_type_repository.select(row['place_type_id'])
        place=Place(row['place_name'],row['description'],place_type ,country, row['visited'],row['rating'], row['id'])
        places.append(place)
    return places