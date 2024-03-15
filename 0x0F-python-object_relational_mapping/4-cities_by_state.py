#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def cities_by_state(username: str, password: str, database_name: str) -> None:
    """
    Connects to the MySQL server and retrieves cities from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Database name.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cursor.execute(query)

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print fetched rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
