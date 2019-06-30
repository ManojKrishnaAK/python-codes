import cx_Oracle
conn=cx_Oracle.connect('hr/hr@localhost/orclpdb')
cur=conn.cursor()
cur.execute('select * from jobs')
for line in cur:
    print(line)
cur.close()
conn.close()
