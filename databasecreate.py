import sqlite3 as lite
import sys

con = None
try:
    con = lite.connect('classSmilarity.db')
    cur = con.cursor()  
    cur.execute("CREATE TABLE courses(course varchar(50), rcourse varchar(50),sim float)")
    courses=open('pairs.txt').readlines()
    for line in courses:
     line1=line.strip()
     (course1,course2,sim)=line1.split('\t')
     cur.execute("insert into courses(course,rcourse, sim) values(?,?,?)",(course1,course2,sim))
    con.commit()
   
        
        
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()