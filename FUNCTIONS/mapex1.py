#mapex1.py
def incr(sal):
	return(sal*1.02)
def disp(lst):
	print("-"*50)
	for sal in lst:
		print("\t",sal)
	print("-"*50)
#main program
print("Enter list of sal of emp separated by comma")
olst=[float(x) for x in input().split(",")]
print("original salaries")
disp(olst)
mobj1=map(incr,olst)
tpl=tuple(mobj1)
print("incremented salaries")
disp(tpl)






