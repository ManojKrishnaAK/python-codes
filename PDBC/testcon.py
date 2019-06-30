#testcon.py
import cx_Oracle,sys
try:
	con=cx_Oracle.connect("hr/hr@localhost/orclpdb")
	if con!=None:
		print("connection obtained from oracle:")
	else:
		print("connection not obtained from oracle:")
		sys.exit()
	cur=con.cursor()
	print("cur obj created and ready to execute any query:")
except cx_Oracle.DatabaseError:
	print("prob in database:")
finally:
	print("i am from finally block")
	if cur:
		cur.close()
		print("cur. closed")
	if con:
		print("con. closed")
		con.close()
