#dynamivrecinsert1.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	#accept the student values from kbd
	while True:	
		print("-"*60)
		sno=int(input("enter Student number:"))
		name=input("enter student name: ")
		marks=float(input("enter Student marks:"))
		addr=input("enter student address: ")
		q="insert into pystudent values(%d,'%s',%f,'%s')"
		cur.execute(q %(sno,name,marks,addr))
		con.commit()
		print("-"*60)
		print("record inserted in table-verify") #step-6
		print("-"*60)
		ch=input("do u want to insert new record(yes/no)")
		if((ch=="NO") or(ch=="no") or(ch=="No")):
			break;
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if con:
		con.close() #step-7
  