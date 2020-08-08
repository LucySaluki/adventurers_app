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

# select all

# select individual

# delete individual

# update individual