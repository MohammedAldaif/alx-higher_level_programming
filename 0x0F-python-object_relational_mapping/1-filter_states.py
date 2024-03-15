#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

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
