DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS place_types;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255),
    visited: BOOLEAN
);

CREATE TABLE place_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(255)
);

CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    place_name VARCHAR (255),
    description VARCHAR(255),
    place_type_id INT REFERENCES place_types(id),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id)
)