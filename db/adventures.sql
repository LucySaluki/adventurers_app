DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    place_name VARCHAR (255),
    description VARCHAR(255),
    place_type VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id)
)