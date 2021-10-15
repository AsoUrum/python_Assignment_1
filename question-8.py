"""

Question 8: Given a two list. Create a third list by picking an odd-index element from the
first list and even index elements from second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

"""
listOne = [3, 6, 9, 12, 15, 18, 21]

listTwo = [4, 8, 12, 16, 20, 24, 28]



listThree = [listTwo[0],listOne[1],listTwo[2],listOne[3],listTwo[4],listOne[5],listTwo[6]]

### Or listThree = [listOne[1],listTwo[0],listOne[3],listTwo[2],listOne[5],listTwo[4],listTwo[2]]

print(listThree)



