#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        #test
        iCreate cursor object
        cursor = db.cursor()

        # Execute SQL query to fetch distinct states
        cursor.execute("SELECT DISTINCT id, name FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    list_states(username, password, database)
