import sqlite3

"""
recruitdb = 'recruits.db'
conn = sqlite3.connect(recruitdb)

c = conn.cursor()
"""

class Memberdb:

    def __init__(self, server):
        self.server = server
        #self.cursor = 0


    def connectdb():
        members = server + 'members.db'
        return sqlite3.connect(members)


    def disconnectdb(self, connection):
        #members = server + 'members.db'
        #connM = sqlite3.connect(members)

        connection.commit()
        connection.close()


    def createtable():
        conn = connectdb()
        c = conn.cursor()

        #(id, name, rating)
        c.execute(
            'CREATE TABLE memberlist(id INTEGER PRIMARY KEY, name STRING, rating INTEGER)')
        conn.disconnectdb(conn)
#
