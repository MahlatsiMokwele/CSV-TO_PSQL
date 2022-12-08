from dotenv import load_dotenv
from config import config
import os
import csv
import psycopg2
import Logging

# Env Sourcing
load_dotenv('.env')
pg_db = os.envriron.get("POSTGRES_DB")
pg_host = os.envriron.get("POSTGRES_HOST")
pg_user = os.envriron.get("POSTGRES_USER")
csv_fil = os.envriron.get("CSV_LOCATION")
pg_port = os.envriron.get("POSTGRES_PORT")
pg_password = os.envriron.get("POSTGRES_PASSWORD")
sql_file = os.envriron.get("SCHEMA_LOCATION")

def database_connection():
# Database Connection
    db_connection = None
    try:
        Logging.info("Connecting to the database...")
        db_connection = psycopg2.connect(
            database=pg_db,
            user=pg_user,
            password=pg_password,
            host=pg_host,
            port=pg_port
        )
    except (Exception, psycopg2.DatabaseError) as e:
        Logging.error(e)
    Logging.info("Database connection established")
    return db_connection

def create_tables():
    # Create tables in db
    db_connection = database_connection()
    try:
        cursor = db_connection.cursor()
        cursor.execute(open(sql_file, 'r').read())
        db_connection.autocommit = True
    except (Exception, psycopg2.DatabaseError) as db_error:
        Logging.error(db_error)
        cursor.rollback()
    
    Logging.info("Query Complete")

def import_csv():
    # Read and import CSV file
    db_connection = database_connection()
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

def main():
    db_connection = database_connection()
    create_tables()
    import_csv()
    db_connection.close()

if __name__ == "__main__":
    main()