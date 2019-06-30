#prog for cal si-----sit.py
p=input("Enter Principle amt: ")
t=input("Enter Time: ")
r=input("Enter Rate of Interest: ")
pv=float(p)
tv=float(t)
rv=float(r)
si=(pv*tv*rv)/100
tamt=pv+si
print("Interrest details")
print("-"*30)
print("Principle amount="+str(pv))
print("Interest rate="+str(rv))
print("Time="+str(tv))
print("Interest on principle="+str(si))
print("Total amount="+str(tamt))
print("-"*30)
