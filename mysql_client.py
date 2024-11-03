from enum import Enum
import mysql.connector
import os
import dotenv
dotenv.load_dotenv()

host = "localhost"
user = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
database = "finances"

class CmdType(Enum):
    INSERT = 1
    QUERY = 2
    UPDATE = 3
    DELETE = 4


def cmd(sql_str, entity, type: CmdType = CmdType.QUERY):
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

        # Execute sql command
        cursor.execute(sql_str, entity)
        

        if type is not CmdType.QUERY:
            cursor.execute(sql_str, entity)
            lastRowId = cursor.lastrowid
            print(f"Last Row ID: {lastRowId}")
            connection.commit()
        else:
            return cursor.fetchall()
            
        
        # close the cursor and connection when finished
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")