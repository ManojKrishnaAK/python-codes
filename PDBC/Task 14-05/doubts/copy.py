sfile=input("enter source file name:")
dfile=input("enter destination file name:")
fp=open(sfile,"r")
cfp=open(dfile,"w")
data=fp.read()
cfp.write(data)
print(sfile,"data copied into",dfile,"--verify")