#recinsert1.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	qry="insert into pystudent values(100,'KVR',94.25,'RMPT')"
	cur.execute(qry) #step-5---static query
	con.commit()
	print("record inserted in table-verify") #step-6
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if con:
		con.close() #step-7
