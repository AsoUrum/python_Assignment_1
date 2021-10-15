"""
Question 4: Given a string and an int n, remove characters from string starting from zero
upto n and return a new string
"""


print ("Question 4 :Given a string and an int n, " +
       "remove characters from string starting from zero upto n and return a new string \n\n\n")
       
anyString = input ("Enter a word to be changed: ")
nNum = int(input("Enter a number: "))

newword = anyString[0:nNum]

print (newword)


