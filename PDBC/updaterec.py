#updaterec.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	q="update pystudent set marks=marks*1.02 where stno=%d"
	sno=int(input("Enter Student Number:"))
	cur.execute(q %sno)
	con.commit()
	print("student marks updated--verity")
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if con:
		con.close() #step-7
  