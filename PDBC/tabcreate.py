#tabcreate.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	qry="create table pystudent(stno number(3),name varchar2(20),marks number(7,2))"  #step-4
	cur.execute(qry) #step-5
	print("table created in oracle db-verify") #step-6
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
