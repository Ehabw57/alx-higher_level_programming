#!/usr/bin/python3
"""This moudle is for task 0"""
from sys import argv
import MySQLdb as mysql
if __name__ == '__main__':
    args = argv[1:]
    db = mysql.connect(host='localhost', port=3306,
                       user=args[0], passwd=args[1], db=args[2])
    cur = db.cursor()
    cur.execute('SELECT cities.name '
                'FROM cities JOIN states '
                'ON states.id = cities.state_id '
                'WHERE states.name = "{}"'.format(args[3]))

    data = cur.fetchall()
    for row in data:
        print(row[0] + ", " if row != data[-1]
              else f"{data[-1][-1]}\n", end='')
    cur.close()
    db.close()
