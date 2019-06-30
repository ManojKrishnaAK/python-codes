#maxmin.py
def findmaxmin(tpl):
	max=tpl[0]
	min=tpl[0]
	print("----------------------------------")
	print("content of tuple:")
	print("----------------------------------")
	for x in tpl:
		print(x)
		if (x>max):
			max=x
		elif (x<min):
			min=x
	return (max,min)


#main prog
tp=(10,34,9,-4,19,6)
max, min=findmaxmin(tp)
print("max element=",max)
print("min element=",min)
print("----------------------------------")