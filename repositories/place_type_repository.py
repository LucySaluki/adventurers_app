from db.run_sql import run_sql

from models.place_types import PlaceType

# save
# create sql and values
# run sql with values
# get back id from database
# return the full place type object
def save(place_type):
    sql = "INSERT INTO place_types(type_name) VALUES(%s) RETURNING ID"
    values =[place_type.type_name]
    result = run_sql(sql, values)[0]
    place_type.id = result['id']
    return place_type

# delete all
# create delete sql
# run sql in database
def delete_all():
    sql = "DELETE FROM place_types"
    run_sql(sql)

# select all
# create and empty object
# create sql
# run sql in database
# got through result and create a place type object and append to the empty object
# return the full list
def select_all():
    place_types = []
    sql = "SELECT * FROM place_types order by place_types.type_name"
    results = run_sql(sql)
    for result in results:
        place_type = PlaceType(result["type_name"], result["id"])
        place_types.append(place_type)
    return place_types

# select individual
# create the sql using the id as only value
# run sql and return only first result (only result)
# create a place type object from the result and return
def select(id):
    sql = "SELECT * FROM place_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    place_type = PlaceType(result["type_name"], result["id"])
    return place_type

# delete individual
# create the sql and run using only the id
def delete(id):
    sql = "DELETE FROM place_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
# create the sql using all fields
# create the values based on the country argument
# run the sql and update the database
def update(place_type):
    sql = "UPDATE place_types SET type_name = %s WHERE id = %s"
    values = [place_type.type_name, place_type.id]
    run_sql(sql, values)
