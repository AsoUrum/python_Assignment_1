"""

Requeting two values from the user,
returning the product if the are less than 1000
else return thier sum.

"""
value1 = int(input("Please enter your first value: "))
value2 = int(input("Please enter your secound value: "))


product = value1 * value2
sumofvalues = value1 + value2

if product < 1000 :
    print("The products of the values entered is ",product)
else :
    print("The sum of the values entered is  ",sumofvalues)

          
             
