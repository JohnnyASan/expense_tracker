import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

host = "localhost"
user = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
database = "finances"

try:
    # Establish a connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute a simple query (e.g., selecting the current database)
    cursor.execute("SELECT DATABASE();")
    database_name = cursor.fetchone()[0]

    print(f"Connected to database: {database_name}")

    # Don't forget to close the cursor and connection when you're done!
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")