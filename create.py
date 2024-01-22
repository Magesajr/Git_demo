import sqlite3  as sq
con=sq.connect('Mydatabase.db')
cur=con.cursor()

command='''
CREATE TABLE  TEST(
id INTEGER PRIMARY KEY,
name VARCHAR (20),
surname VARCHAR (20),
gender CHAR (1),
joining_date DATE);
'''

cur.execute(command)

command='''
INSERT INTO TEST VALUES(001,'magesa', 'sam' ,'M', '2000-07-08')'''

cur.execute(command)

command='''
INSERT INTO TEST VALUES(002,'kabula', 'mark' ,'F', '2000-07-08')'''
cur.execute(command)

command='''
INSERT INTO TEST VALUES(003,'rashid', 'shaban' ,'M', '2000-03-08')'''
cur.execute(command)

command='''
INSERT INTO TEST VALUES(004,'amina', 'sparrow','F', '2000-07-03')'''
cur.execute(command)





con.commit()
con.close()