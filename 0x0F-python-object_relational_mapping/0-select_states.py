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

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Close cursor and database connection
    cursor.close()
    db.close()

    # Use a set to store unique states
    unique_states = set()

    # Filter out duplicate entries
    for state in states:
        unique_states.add(state)

    # Print the unique states
    for state in unique_states:
        print(state)


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
