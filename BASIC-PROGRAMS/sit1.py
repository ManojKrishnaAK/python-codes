#prog for cal si-----sit1.py
p=float(input("Enter Principle amt: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate of Interest: "))
si=(p*t*r)/100
tamt=p+si
print("Interrest details")
print("-"*30)
print("Principle amount="+str(p))
print("Interest rate="+str(r))
print("Time="+str(t))
print("Interest on principle="+str(si))
print("Total amount="+str(tamt))
print("-"*30)
