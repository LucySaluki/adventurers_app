from db.run_sql import run_sql

from models.place_types import PlaceType

# save
def save(place_type):
    sql = "INSERT INTO place_types(type_name) VALUES(%s) RETURNING ID"
    values =[place_type.type_name]
    result = run_sql(sql, values)[0]
    place_type.id = result['id']
    return place_type

# delete all
def delete_all():
    sql = "DELETE FROM place_types"
    run_sql(sql)

# select all
def select_all():
    place_types = []
    sql = "SELECT * FROM place_types order by place_types.type_name"
    results = run_sql(sql)
    for result in results:
        place_type = PlaceType(result["type_name"], result["id"])
        place_types.append(place_type)
    return place_types

# select individual
def select(id):
    sql = "SELECT * FROM place_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    place_type = PlaceType(result["type_name"], result["id"])
    return place_type

# delete individual
def delete(id):
    sql = "DELETE FROM place_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
def update(place_type):
    sql = "UPDATE place_types SET type_name = %s WHERE id = %s"
    values = [place_type.type_name, place_type.id]
    print(place_type.type_name)
    print(place_type.id)
    run_sql(sql, values)
