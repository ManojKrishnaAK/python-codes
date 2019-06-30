#deleterec.py
import cx_Oracle,sys   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	q="delete pystudent where name='%s' "
	while True:
		sname=input("Enter Student Name to delete:")
		cur.execute(q %sname)
		con.commit()
		if (cur.rowcount>0):
			print("student record deleted-verity")
		else:
			print("student record not  deleted-verity")
		ch=input("Do u want delete record again(Yes/No):")
		if ((ch=="NO") or (ch=="No") or (ch=="no")):
			sys.exit()
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if con:
		con.close() #step-7
  