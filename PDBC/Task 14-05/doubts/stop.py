fname=input("enter filename:")
fp=open(fname,"w")
data=input("enter ur text(to stop enter stop)\n")
while(data!="stop"):
          fp.write(data +"\n")
          data=input()
print("****data written to the file****")
          
