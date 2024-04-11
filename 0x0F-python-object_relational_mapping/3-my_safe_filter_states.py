#!/usr/bin/python3
"""This moudle is a secure version of the last script"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    args = argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=args[0], passwd=args[1], db=args[2])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    WHERE BINARY `name` LIKE %s
    ORDER BY states.id ASC""", (args[3],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
