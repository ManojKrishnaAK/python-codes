#finds biggest of three nos
a=int(input("Enter First Value: "))
b=int(input("Enter Second Value: "))
c=int(input("Enter Third Value: "))
big=a
if (b>big):
	big=b
if (c>big):
	big=c
print("biggest=",big)