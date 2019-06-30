#Python program to extract emails From the Given data By Regular Expression. 
import re  
# Example string  
s = 'Hello from kvr1.java@gmail.com to priya@yahoo.com, rakesh123@gmail.com , raju_python@hotmail.com , mahesh@yahoo.com about the meeting  @6PM'
  
# here \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
matchlst = re.findall('\S+@\S+', s)     
  
# Printing  List of mails
for mail in matchlst:
	print(mail) 