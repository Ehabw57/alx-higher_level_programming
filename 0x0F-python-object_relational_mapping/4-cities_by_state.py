#!/usr/bin/python3
""" This scirpt is used to list all cities and its states
using MySQLdb libraly"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    args = argv[1:]
    conn = MySQLdb.connect(user=args[0], passwd=args[1],
                           db=args[2], host='localhost', port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
