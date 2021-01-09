import psycopg2
from flask import Flask, current_app
from flask import g

# Connect to the db
conn = psycopg2.connect(database='usajobs_dev',
                        user='postgres',
                        password='postgres')
cur = conn.cursor()

def build_from_record(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def build_from_records(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def drop_all_tables(conn, cur):
    table_names = ['positions', 'salary', 'locations', 'applications', 'terms']
    drop_tables(table_names, conn, cur)
    
def drop_tables(table_names, conn, cur):
    for table_name in table_names:
        drop_records(table_name, conn, cur)

def drop_records(table_name, conn, cur):
    cur.execute(f"DROP {table_name} [IF EXISTS];")

def find(Class, id, cur):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE id = %s"
    cur.execute(sql_str, (id, ))
    record = cur.fetchone()
    return build_from_record(Class, record)

def find_all(Class, id, cur):
    sql_str = f"SELECT * FROM {Class.__table__}"
    cur.execute(sql_str)
    records = cur.fetchall()
    return [build_from_record(Class, record) for record in records]

def find_by_name(Class, name, cur):
    query = f"""SELECT * FROM {Class.__table__} WHERE name = %s """
    cur.execute(query, (name, ))
    record = cur.fetchone()
    obj = build_from_record(Class, record)
    return obj

def find_or_build_by_name(Class, name, cur):
    obj = Class.find_by_name(name, cur)
    if not obj:
        obj = Class()
        obj.name = name
    return obj

def find_or_create_by_name(Class, name, conn, cur):
    obj = find_by_name(Class, name, cur)
    if not obj:
        new_obj = Class()
        new_obj.name = name
        obj = save(new_obj, conn, cur)
    return obj

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(user='p911',
                                password='postgres',
                                dbname=current_app.config['usajobs_dev'])
    return g.db

def keys(obj):
    position_attrs = obj.__dict__
    selected = [attr for attr in obj.columns if attr in position_attrs.keys()]

def save(obj, conn, cur):
    s_str = ', '.join(len(values(obj)) * ['%s'])
    venue_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
    cur.execute(venue_str, list(values(obj)))

def values(obj):
    position_attrs = obj.__dict__
    return [
        position_attrs[attr] for attr in obj.columns
        if attr in position_attrs.keys()
    ]

# Close the cursor
cur.close()

# Close the connection
conn.close()