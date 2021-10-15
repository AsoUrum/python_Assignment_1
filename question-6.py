"""
Question 6: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of
s1
"""

#first string is a lsit of strings
string1 = ["welcome", "to" ,"america", "yes"]

string2 = "Thank"

l= len(string1)
print(l//2)
string1.insert(l//2,string2)

string3 = string1


print("String one: ", string1)

print("String two: ",string2)

print("String three: ",string3)





"""
s1 = "welcome"
s2 = "AS0"
l=len(s1)
print(l)

print(s1)
"""
