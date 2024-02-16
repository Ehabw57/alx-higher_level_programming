#!/usr/bin/python3
"""This moudle is for task 0"""
from sys import argv
import MySQLdb as mysql
if __name__ == '__main__':
    args = argv[1:]
    db = mysql.connect(host='localhost', port=3306,
                       user=args[0], passwd=args[1], db=args[2])
    cur = db.cursor()
    cmd = 'SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY id ASC'
    cur.execute(cmd.format(args[3]))

    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
