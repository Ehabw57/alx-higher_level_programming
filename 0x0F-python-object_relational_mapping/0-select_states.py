#!/usr/bin/python3
"""This moudle is for task 0"""
from sys import argv
import MySQLdb as mysql
if __name__ == '__main__':
    args = argv[1:]
    db = mysql.connect(host='localhost', port=3306,
                       user=args[0], passwd=args[1], db=args[2])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
