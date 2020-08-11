from db.run_sql import run_sql

from models.countries import Country

# save
# create sql and values
# run sql with values
# get back id from database
# return the full country object
def save(country):
    sql = "INSERT INTO countries(name,continent,visited) VALUES(%s,%s, %s) RETURNING ID"
    values =[country.name, country.continent, country.visited]
    result = run_sql(sql, values)[0]
    country.id = result['id']
    return country

# delete all
# create delete sql
# run sql in database
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

# select all
# create and empty object
# create sql
# run sql in database
# got through result and create a country object and append to the empty object
# return the full list
def select_all():
    countries = []
    sql = "SELECT * FROM countries order by countries.name"
    results = run_sql(sql)
    for result in results:
        country = Country(result["name"], result ['continent'], result['visited'], result["id"])
        countries.append(country)
    return countries

# select individual
# create the sql using the id as only value
# run sql and return only first result (only result)
# create a country object from the result and return
def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = Country(result["name"], result ['continent'], result['visited'],result["id"])
    return country

# delete individual
# create the sql and run using only the id
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update individual
# create the sql using all fields
# create the values based on the country argument
# run the sql and update the database
def update(country):
    sql = "UPDATE countries SET (name, continent, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.visited, country.id]
    run_sql(sql, values)

#update country to reflect new place visited
# initiated whenever a place is added or edited
# create the sql to update visited to true if any of the associated places have been visited field using id 
# run sql
def update_visited(id):
    sql = "update countries set visited = a.visited from (select places.country_id, case when sum(visited_true) = 0 then False else True end as visited from (select country_id, case when visited = True then 1 else 0 end as visited_true from places) as places group by country_id) as a where a.country_id=countries.id and countries.id = %s"
    values = [id]
    run_sql(sql, values)