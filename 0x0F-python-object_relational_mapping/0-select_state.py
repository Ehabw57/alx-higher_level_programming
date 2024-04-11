#!/usr/bin/python3
"""A moudlue that lists all the states
in htbn_0e_0d_usa database using MySQLdb"""
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='ehab', db='hbtn_0e_0_usa')
cur = conn.cursor()
cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
