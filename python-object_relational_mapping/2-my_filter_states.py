#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd='',
                           db=sys.argv[3],
                           charset="utf8")
    
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE BINARY '{}'\
                ORDER BY `id` ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()