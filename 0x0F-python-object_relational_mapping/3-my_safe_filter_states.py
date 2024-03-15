#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the provided argument, using safe parameterized queries.
"""

import MySQLdb
import sys


def safe_filter_states(username: str, password: str, database_name: str, state_name: str) -> None:
    """
    Connects to the MySQL server and retrieves states matching the provided
    state name from the specified database using safe parameterized queries.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Database name.
        state_name (str): State name to search for.

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

    # Execute SQL query with parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print fetched rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    

    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
