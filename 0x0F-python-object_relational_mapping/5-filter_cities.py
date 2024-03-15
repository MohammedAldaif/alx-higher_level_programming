#!/usr/bin/python3
"""
Script that lists cities and states.
"""

import MySQLdb
import sys


def filter_cities(username: str, password: str, database_name: str, state_name: str) -> None:
    """
    Connects to the MySQL server and lists all cities of the specified state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Database name.
        state_name (str): State name.

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
            SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            """
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    if result:
        print(result)
    else:
        print("No cities found for the state:", state_name)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
