"""
Question 7: Find all occurrences of “USA” in given string (uppercase and lowercase).
Welcome to USA. usa awesome, isn't it?

"""
#the given string
str1 = "Welcome to USA. usa awesome, isn't it"

#the word to findin uppercase
tofind= "USA"

# the word to find in lowercase
tofind.lower()

# the uumber of occurances of the String "USA" both in capital and small letters is 
num =  str1.count(tofind) +  str1.count(tofind.lower())


print("the number of occurances of the String 'USA' both in capital and small letters is = ", num)


print(str1[11:14])

print(str1[16:19])
