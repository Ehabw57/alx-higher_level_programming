#!/usr/bin/python3
"""A moudle that list all states statrt with
N (capital n)"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    args = argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=args[0], passwd=args[1], db=args[2])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    WHERE BINARY `name` LIKE 'N%'
    ORDER BY states.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
