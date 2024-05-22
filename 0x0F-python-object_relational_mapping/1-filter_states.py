#!/usr/bin/python3
import MySQLdb
import sys

def list_states_starting_with_N(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select distinct states starting with 'N' and eliminate duplicates
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' GROUP BY id, name ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract username, password, and database from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states starting with 'N'
    list_states_starting_with_N(username, password, database)
