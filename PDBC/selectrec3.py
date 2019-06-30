#selectrec3.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	ncur=con.cursor() #step-3
	q="select * from pystudent"
	cur.execute(q)
	q1="insert into javastudent values(%d,'%s',%f,'%s')"
	rec1=cur.fetchone()
	while rec1!=None:
		ncur.execute(q1%(rec1[0],rec1[1],rec1[2],rec1[3]))
		con.commit()
		rec1=cur.fetchone()
	print("records transfered--verify")
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if ncur:
		ncur.close()    #step-7
	if con:
		con.close() #step-7
