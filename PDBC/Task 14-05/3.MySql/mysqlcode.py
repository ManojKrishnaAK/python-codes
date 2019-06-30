import pymysql
conn = pymysql.connect("localhost","root","root","scott")#host,user,pwd,db
#cursor obj
cur = conn.cursor()
sql=("select * from employee")
cur.execute(sql)
#data=cur.fetchall()
for i in cur:
	print(i)