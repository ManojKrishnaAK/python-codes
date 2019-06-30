#tabalter.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	qry="alter table pystudent add(addr varchar2(20))"  #step-4
	#qry="alter table pystudent modify(stno number(6))"  #step-4
	cur.execute(qry) #step-5
	print("table altered in oracle db-verify") #step-6
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	print("i am from finally block")
	if cur:
		cur.close()    #step-7
		print("cur. closed")
	if con:
		print("con. closed")
		con.close() #step-7
