import sqlite3 as lite
import sys
con = None
pairs=[]
try:
    con = lite.connect('classSmilarity.db')
    cur = con.cursor()  
    
    cur.execute("select * from courses where sim>=0 and sim<=0.25")
    out1=open('course0.25.txt','w')
    out1.write("Source Course"+"\t"+"Target Course")
    for row in cur:
        t1=row[1]+row[0]
        t2=row[0]+row[1]
        if t1 in pairs: continue
        pairs.append(t2)
        out1.write("\n%s\t%s" %(row[0],row[1]))
    cur.execute("select * from courses where sim>0.25 and sim<=0.5")
    out2=open('course0.25-0.5.txt','w')
    out2.write("Source Course"+"\t"+"Target Course")
    for row in cur:
        t1=row[1]+row[0]
        t2=row[0]+row[1]
        if t1 in pairs: continue
        pairs.append(t2)
        out2.write("\n%s\t%s" %(row[0],row[1]))
    cur.execute("select * from courses where sim>0.5 and sim<=0.75")
    out3=open('course0.5-0.75.txt','w')
    out3.write("Source Course"+"\t"+"Target Course")
    for row in cur:
        t1=row[1]+row[0]
        t2=row[0]+row[1]
        if t1 in pairs: continue
        pairs.append(t2)
        out3.write("\n%s\t%s" %(row[0],row[1]))
    cur.execute("select * from courses where sim>0.75 and sim<=1")
    out4=open('course0.75-1.txt','w')
    out4.write("Source Course"+"\t"+"Target Course")
    for row in cur:
        t1=row[1]+row[0]
        t2=row[0]+row[1]
        if t1 in pairs: continue
        pairs.append(t2)
        out4.write("\n%s\t%s" %(row[0],row[1]))    
    

        
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()