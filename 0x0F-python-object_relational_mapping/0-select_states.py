#!/usr/bin/python3
"""A moudlue that lists all the states
in htbn_0e_0d_usa database using MySQLdb"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    args = argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=args[0], passwd=args[1], db=args[2])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    ORDER BY states.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
