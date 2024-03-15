#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def filter_states(username: str, password: str, database_name: str) -> None:
    """
    Connects to the MySQL server and retrieves states starting with 'N'
    from the specified database.

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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
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
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
