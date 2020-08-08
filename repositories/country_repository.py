from db.run_sql import run_sql

from models.countries import Country


# save
def save(country):
    sql = "INSERT INTO countries(name) VALUES(%s) RETURNING ID"
    values =[country.name]
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
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for result in results:
        country = Country(result["name"], result["id"])
        countries.append(country)
    return countries

# select individual
def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = Country(result["name"], result["id"])
    return country

# delete individual
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
# update individual