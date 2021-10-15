"""
Question 5: Given a list of ints, return True if first and last number of a list is same

"""

question = "Question 5: Given a list of ints, return True if first and last number of a list is same"
print( question, "\n\n\n")

### give the list of int


### give the list of int
listOfInt=[1,2,3,4,5,9,10,8,25.6]
print("Given this list of int ", listOfInt , "\n" ) 


# First interger int the list is
print ("First interger int the list is", listOfInt[0],"\n" )


# last interger in the list is
l =len(listOfInt)
print ("Last interger int the list is", listOfInt[l-1],"\n" )## or print(listOfInt[-1])


# Is the fisrt interger of the list same as the last interger in the list

print ("Is the fisrt interger of the list same as the last interger in the list?\n","=======>",listOfInt[0] is listOfInt[l-1])




