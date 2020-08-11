from db.run_sql import run_sql
from models.places import Place
from models.countries import Country
from models.place_types import PlaceType

import repositories.country_repository as country_repository
import repositories.place_type_repository as place_type_repository

# save
# create sql and values
# run sql with values
# get back id from database
# return the full place object
def save(place):
    sql = "INSERT INTO places (place_name, description, place_type_id, country_id, visited, rating) VALUES (%s, %s, %s,%s, %s, %s) RETURNING id"
    values =[place.place_name, place.description, place.place_type.id, place.country.id, place.visited, place.rating]
    result = run_sql(sql,values)[0]
    place.id = result['id']
    country_repository.update_visited(place.country.id)
    return place

# delete all
# create delete sql
# run sql in database
def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)

# select all
# create and empty object
# create sql
# run sql in database
# got through result and pick up the country object and place type object from the id
# create a place object and append to the empty object
# return the full list
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
# create the sql using the id as only value
# run sql and return only first result (only result)
# search for the country object and place type object based on id
# create a place object from the result and return
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
# create the sql and run using only the id
def delete(id):
    sql = "DELETE FROM places WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
# create the sql using all fields
# create the values based on the country argument
# run the sql and update the database
def update(place):
    sql = "UPDATE places SET (place_name, description, place_type_id, country_id, visited, rating) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [place.place_name, place.description, place.place_type.id, place.country.id, place.visited, place.rating, place.id]
    print(place.id)
    run_sql(sql, values)

# select filtered
# create and empty object
# create the sql based on the visited fields and use the visited value only
# run sql
# with all the results retured use the country id to select the country object
# use the place_type_id to select the place type object
# create a place object base on the returned results and the new objects above
# append to the empty object created
# return places object
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

# select search
# create and empty object
# create the sql based on the continent field only across the two tables with a join
# run sql
# with all the results retured use the country id to select the country object
# use the place_type_id to select the place type object
# create a place object base on the returned results and the new objects above
# append to the empty object created
# return places object
def select_search(continent):
    places = []
    sql = "SELECT places.* FROM places INNER JOIN countries ON places.country_id = countries.id WHERE countries.continent = %s"
    values = [continent]
    results = run_sql(sql,values)

    for row in results:
        country = country_repository.select(row['country_id'])
        place_type = place_type_repository.select(row['place_type_id'])
        place=Place(row['place_name'],row['description'],place_type ,country, row['visited'],row['rating'], row['id'])
        places.append(place)
    return places