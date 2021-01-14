import sqlite3

"""
recruitdb = 'recruits.db'
conn = sqlite3.connect(recruitdb)

c = conn.cursor()
"""

class Memberdb:
    def __init__(self, server_id):
        self.server = server_id
        #self.cursor = 0


    def connectdb(self):
        members = self.server + 'members.db'
        return sqlite3.connect(members)


    def disconnectdb(self, connection, cursor):
        connection.commit()
        cursor.close()


    def checktable(self):
        conn = self.connectdb()
        c = conn.cursor()

        try:
            c.execute('SELECT * FROM memberlist')

        except Exception as e:
            #(id in table, name, discord id,rating)
            c.execute('CREATE TABLE memberlist(id INTEGER PRIMARY KEY, name STRING, discordid INTEGER, rating INTEGER)')

            conn.commit()

        finally:
            c.close()

    def nodupe(self, id):
        conn = self.connectdb()
        c = conn.cursor()

        t = (id,)

        c.execute('SELECT * FROM memberlist WHERE discordid=?', t)
        if c.fetchone():
            return False
        else:
            return True

    def addMember(self, member, id):
        newface = False
        self.checktable()

        conn = self.connectdb()
        c = conn.cursor()

        line = (member, id, 1)

        if self.nodupe(id):
            c.execute('INSERT INTO memberlist(name, discordid, rating) VALUES(?, ?, ?)', line)
            newface = True

        self.disconnectdb(conn, c)
        return newface

    def getRatingList(self):
        self.checktable()

        conn = self.connectdb()
        c = conn.cursor()

        c.execute('SELECT name, rating FROM memberlist')

        list = c.fetchall()
        self.disconnectdb(conn, c)

        return list
