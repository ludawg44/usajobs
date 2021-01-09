from db import *
import psycopg2


# Connect to the db
conn = psycopg2.connect(
    database = 'usajobs_dev',
    user = 'postgres',
    password = 'postgres'
)

# Cursor
cur = conn.cursor()

# CREATE TABLE IF NOT EXISTS positions(
#     id serial PRIMARY KEY,
#     usa_jobs_id VARCHAR(255),
#     position_title CHAR(255),
#     position_url CHAR(255));
cur.execute(
    'INSERT INTO positions (usa_jobs_id, position_title, position_url) values (%s, %s, %s)',
    ('GSFC-21-DE-10998370-RW', 'Computer Engineer',
     'https://www.usajobs.gov:443/GetJob/ViewDetails/588432600'))
conn.commit()

# CREATE TABLE IF NOT EXISTS salary(
#     id serial PRIMARY KEY,
#     position_id INT,
#     minimum VARCHAR(255),
#     maximum VARCHAR(255),
#     rate_interval CHAR(255));
cur.execute(
    'INSERT INTO salary (position_id, minimum, maximum, rate_interval) values (%s, %s, %s, %s)',
    ('GSFC-21-DE-10998370-RW', '50860.0', '94581.0', 'Per Year'))
conn.commit()

# CREATE TABLE IF NOT EXISTS locations(
#     id serial PRIMARY KEY,
#     position_id VARCHAR(255),
#     country_code CHAR(255),
#     country_sub_division_code CHAR(255),
#     city_name CHAR(255),
#     longitude DECIMAL,
#     latitude DECIMAL);
cur.execute(
    'INSERT INTO locations (position_id, country_code, country_sub_division_code, city_name, longitude, latitude) values (%s, %s, %s , %s, %s, %s)',
    ('GSFC-21-DE-10998370-RW', 'United States', 'Maryland',
     'Greenbelt, Maryland', -76.8789, 39.0002632))
conn.commit()

# CREATE TABLE IF NOT EXISTS applications(
#     applications_id  serial PRIMARY KEY,
#     position_id VARCHAR(255),
#     publication_start_date VARCHAR(255),
#     application_close_date VARCHAR(255));
cur.execute(
    'INSERT INTO applications (position_id, publication_start_date, application_close_date) values (%s, %s, %s)',
    ('GSFC-21-DE-10998370-RW', '2021-01-05', '2021-01-12'))
conn.commit()

# CREATE TABLE IF NOT EXISTS terms(
#     id serial PRIMARY KEY,
#     applications_id INT,
#     travel_percentages VARCHAR(255),
#     position_schedule_name CHAR(255),
#     position_offering_type_name CHAR(255),
#     security_clearance VARCHAR(255)
#     PRIMARY KEY (id),
#     CONSTRAINT fk_applications
#         FOREIGN KEY(applications_id)
#             REFERENCES applications(applications_id));
cur.execute(
    'INSERT INTO terms (applications_id, travel_percentages, position_schedule_name, position_offering_type_name, security_clearance) values (%s, %s, %s, %s. %s)',
    (1, '0', 'Full-Time', 'Permanent', 'Not Required'))
conn.commit()


# Close the cursor
# cur.close()

# # Close the connection
# conn.close()