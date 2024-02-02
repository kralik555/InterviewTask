import psycopg2
import pandas as pd
import csv

def create_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS flats")
    except:
        print("Flats does not exist")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flats (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            image1 VARCHAR(255),
            image2 VARCHAR(255),
            image3 VARCHAR(255),
            number INTEGER
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
        'port': 5432 
    }
    
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
            title, image1, image2, image3, number = row
            cursor.execute("INSERT INTO flats (title, image1, image2, image3, number) VALUES (%s, %s, %s, %s, %s)", row)

    conn.commit()
    cursor.close()
    conn.close()


def fetch_ads_data():
    db_config = {
        'host': 'db',  # Use the service name defined in your Docker Compose for the database host
        'dbname': 'flats',
        'user': 'kraljak',
        'password': '123456',
        'port': 5432
    }
    
    conn = psycopg2.connect(
        host=db_config['host'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        port=db_config['port']
    )
    
    query = "SELECT title, image1, image2, image3 FROM flats ORDER BY number"
    ads_df = pd.read_sql(query, conn)
    
    ads_dict = ads_df.to_dict(orient='records')
    conn.close()
    return ads_dict
