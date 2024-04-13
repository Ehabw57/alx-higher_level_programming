#!/usr/bin/python3
"""script that takes in the name of a state,
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    args = argv[1:]
    conn = MySQLdb.connect(user=args[0], passwd=args[1],
                           db=args[2], host='localhost', port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC""", (args[3],))
    cities = cur.fetchall()
    print(*[city[0] for city in cities], sep=", ", end="")
    print()
