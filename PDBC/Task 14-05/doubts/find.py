fname=input("enter file name to find number of words,lines and characters:")
fp=open(fname,"r")
cw=0
cc=0
cl=0
for line in fp:
    words=line.split()
    cw=cw+len(words)
    cl=cl+1
    cc=cc+len(line)
print("number of characters",cc)
print("number of words",cw)
print("number of lines",cl)
