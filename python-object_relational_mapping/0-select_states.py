#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd='',
                         db=sys.argv[3],
                         charset="utf8")
"""This line creates a cursor to execute SQL queries on the database."""
cur = db.cursor()
"""This line executes an SQL query to select all columns (*) from the "states" table, sorted by ID in ascending order (ASC)."""
cur.execute("SELECT * FROM `states` ORDER BY `id`ASC")
"""This line retrieves all resulting rows from the previously executed query."""
query_rows = cur.fetchall()
"""This loop iterates over each resulting row."""
for row in query_rows:
    """This line prints each row."""
    print(row)
"""This line closes the cursor."""
cur.close()
"""This line closes the database connection."""
db.close()
