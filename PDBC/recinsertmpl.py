#recinsertmpl.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	qry="insert into pystudent values(:stno,:name,:marks,:addr)" #step-4
	records=[ (102,'rahul',67.89,'USA'),
					(103,'mahesh',87.89,'UK'),
					(104,'arpitha',97.89,'AUS'),
					(105,'ramu',57.89,'IND')  ]
	cur.executemany(qry,records) #step-5---static query
	con.commit()
	print("records inserted in table-verify") #step-6
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()  #step-7
	if con:
		con.close() #step-7
