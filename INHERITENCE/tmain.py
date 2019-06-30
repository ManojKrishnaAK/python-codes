#main program---teachermain.py
from Teacher import Teacher
t=Teacher()
t.setId(10)
t.setName("sathya")
t.setAddr("ampt")
print("Teacher Id=",t.getId())
print("Teacher Name=",t.getName())
print("Teacher Addr=",t.getAddr())
