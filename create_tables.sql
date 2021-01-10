DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS terms;

CREATE TABLE IF NOT EXISTS positions(
    id serial PRIMARY KEY,    
    usa_jobs_id VARCHAR(255),
    position_title CHAR(255),
    position_url CHAR(255));

CREATE TABLE IF NOT EXISTS salary(
    id serial PRIMARY KEY,
    position_id VARCHAR(255),
    minimum VARCHAR(255),
    maximum VARCHAR(255),
    rate_interval CHAR(255));

CREATE TABLE IF NOT EXISTS locations(
    id serial PRIMARY KEY,
    position_id VARCHAR(255),
    country_code CHAR(255),
    country_sub_division_code CHAR(255),
    city_name CHAR(255),
    longitude DECIMAL,
    latitude DECIMAL);

CREATE TABLE IF NOT EXISTS applications(
    id serial PRIMARY KEY,
    position_id VARCHAR(255),
    publication_start_date VARCHAR(255),
    application_close_date VARCHAR(255));

CREATE TABLE IF NOT EXISTS terms(
    id serial PRIMARY KEY,
    position_id VARCHAR(255),
    travel_percentages VARCHAR(255),
    position_schedule_name CHAR(255),
    position_offering_type_name CHAR(255),
    security_clearance VARCHAR(255));