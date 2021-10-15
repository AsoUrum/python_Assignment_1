"""
Given a string of odd length 7, return the middle char of the word
"""

word = input("Please Enter an odd number word with characters greater that 7: ")


wordlenght= int(len(word))
odd = wordlenght%2

while ( not(wordlenght >=7 and odd == 1)):
    print("invalid word length, or not an odd nunber characters. Try again")
    word = input("Please Enter an odd number word with characters greater that 7: ")
    
   
    wordlenght= int(len(word))
    odd = wordlenght%2



start = (wordlenght//2)-1
end = start + 3
result = word[start:end]
print("The 3 middle character to the word entered are ","{", result[0],"}","{",result[1],"}",  "{", result[2],"}")

  
"""
word = input("Please Enter an odd number word with characters greater that 7: ")
wordlenght= int(len(word))
odd = wordlenght%2
if wordlenght >6 and odd == 1:
    start = (wordlenght//2)-1
    end = start + 3
    result = word[start:end]
    print("The 3 middle character to the word entered are ","{", result[0],"}","{",result[1],"}",  "{", result[2],"}")
else :
    print("invalid word length, or not an odd nunber characters. Try again")
"""




