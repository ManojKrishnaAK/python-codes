#lambdaex4.py
big=lambda m,n: m if (m>n) else n   # lambda function
print("biggest of {} and {}={}".format(10,20,big(10,20)))
print("biggest of {} and {}={}".format(-2,45,big(-2,45)))
print("biggest of {} and {}={}".format(-12,-78,big(-12,-78)))