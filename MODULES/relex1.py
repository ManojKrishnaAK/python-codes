#relex1.py---main program for reloading the module
import mul
import time,imp;
mul.cal()
print("going to sleeping---do the changes in mul module...")
time.sleep(10)
print("come out of sleeping...")
imp.reload(mul)
mul.cal()
print("going to sleeping again...do the changes in mul module")
time.sleep(10)
print("come out of sleeping again..")
imp.reload(mul)
mul.cal()