from db.run_sql import run_sql

from models.countries import Country

# save
def save(country):
    sql = "INSERT INTO countries(name,continent,visited) VALUES(%s,%s, %s) RETURNING ID"
    values =[country.name, country.continent, country.visited]
    result = run_sql(sql, values)[0]
    country.id = result['id']
    return country

# delete all
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

# select all
def select_all():
    countries = []
    sql = "SELECT * FROM countries order by countries.name"
    results = run_sql(sql)
    for result in results:
        country = Country(result["name"], result ['continent'], result['visited'], result["id"])
        countries.append(country)
    return countries

# select individual
def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = Country(result["name"], result ['continent'], result['visited'],result["id"])
    return country

# delete individual
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
def update(country):
    sql = "UPDATE countries SET (name, continent,visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.visited, country.id]
    run_sql(sql, values)

#update country to reflect new place visited
def update_visited(id):
    sql = "UPDATE countries SET visited = True WHERE id = %s"
    values = [id]
    run_sql(sql, values)