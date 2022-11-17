from dotenv import load_dotenv
from config import config
import os
import csv
import psycopg2

# Env Sourcing
load_dotenv('.env')
pg_db = os.envriron.get("POSTGRES_DB")
pg_host = os.envriron.get("POSTGRES_HOST")
pg_user = os.envriron.get("POSTGRES_USER")
csv_fil = os.envriron.get("CSV_LOCATION")
pg_port = os.envriron.get("POSTGRES_PORT")
pg_password = os.envriron.get("POSTGRES_PASSWORD")

# Database Connection 
db_connection = psycopg2.connect(
    database=pg_db,
    user=pg_user,
    password=pg_password,
    host=pg_host,
    port=pg_port
)

def create_tables():
    # Create tables in db
    sql_query = (
        """
        CREATE SCHEMA IF NOT EXISTS road_segments;
        """,
        """
        CREATE TABLE IF NOT EXISTS road_segments.202212000_road_segments as (
            feat_id uuid,
            geom public.geometry,
            pos_azimuth double precision,
            neg_azimuth double precision,
            pos_passenger numeric,
            pos_truck numeric,
            pos_private_bus numeric,
            pos_public_bus numeric,
            pos_other numeric,
            neg_passenger numeric,
            neg_truck numeric,
            neg_private_bus numeric,
            neg_public_bus numeric,
            neg_other numeric
        ) 
        """
    )
    try:
        db_connection.autocommit = True
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
    except (Exception, psycopg2.DatabaseError) as db_error:
        print(db_error)

def import_csv():
    # Read and import CSV file
    with open(csv_fil, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for each_row in csv_reader:
            sql_insert = (
                """
                INSERT INTO road_segments.202212000_road_segments VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                each_row
            )
            try:
                db_connection.autocommit = True
                cursor = db_connection.cursor()
                cursor.execute(sql_insert)
                cursor.close()
            except (Exception, psycopg2.DatabaseError) as db_error:
                print(db_error)
            finally:
                if db_connection is not None:
                    db_connection.close()

if __name__ == "__main__":
    create_tables()
    import_csv()