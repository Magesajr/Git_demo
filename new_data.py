import sqlite3  as sq
con=sq.connect('simple.db')
cur=con.cursor()


#command='''
#INSERT INTO Magesa VALUES(1,'karimu', 'shaban','F', '1999-8-9')'''
#cur.execute(command)

command=''' DELETE FROM Magesa'''

for i in range(20):
  cur.execute(command)


con.commit()
con.close()