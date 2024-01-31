import psycopg2
import pandas as pd
import csv

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flats (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            image VARCHAR(255)
        );
    """)
    conn.commit()
    cursor.close()

def insert_data(file_path):
    db_config = {
        'host': 'db',
        'dbname': 'flats',
        'user': 'kraljak',
        'password': '123456',
        'port': 5432  # default PostgreSQL port
    }
    
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host=db_config['host'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        port=db_config['port']
    )

    create_table(conn)

    cursor = conn.cursor()
    
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            title, image = row
            cursor.execute("INSERT INTO flats (title, image) VALUES (%s, %s)", row)

    conn.commit()
    cursor.close()
    conn.close()
