import sqlite3

"""
recruitdb = 'recruits.db'
conn = sqlite3.connect(recruitdb)

c = conn.cursor()
"""

def connectMemberdb():
    members = 'members.db'
    connM = sqlite3.connect(members)

    c = connM.cursor()
#
