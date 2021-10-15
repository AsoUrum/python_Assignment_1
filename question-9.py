
"""
Question 9: Given an input list removes the element at index 4 and add it to the 2nd
position and also, at the end of the list
List = [54, 44, 27, 79, 91, 41]
"""


#Given this list
List = [54, 44, 27, 79, 91, 41]
print("Given this list -->", List, "\n")

#removing the element in the 4th index
itm = List.pop(4-1) # because the index starts at zero, the 4th index will be 4-1
print("removing the element in the 4th index -->",List, "\n")

#adding the removed element to the 2nd position
List.insert(1,itm)
print("adding the removed element to the 2nd position -->",List, "\n")

#adding the removed element to the end position 
List.insert(6,itm)
print("adding the removed element to the end position -->",List, "\n")
