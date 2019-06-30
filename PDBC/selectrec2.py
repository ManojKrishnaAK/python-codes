#selectrec2.py
import cx_Oracle   #step-1
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")  #step-2
	cur=con.cursor() #step-3
	q="select * from pystudent"
	cur.execute(q)
	print("-"*60)
	print("\t\tStudent Records")
	print("-"*60)
	recs=cur.fetchmany()
	for rec1 in recs:
		print("\t{}\t{}\t{}\t{}".format(rec1[0],rec1[1],rec1[2],rec1[3]))
	print("-"*60)
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	if cur:
		cur.close()    #step-7
	if con:
		con.close() #step-7
  