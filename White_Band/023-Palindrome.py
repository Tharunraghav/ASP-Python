
word=input("enter the word:")
reversed_word=word[::-1]
print(reversed_word)
if word==reversed_word:
    print("It is palindrome")
else:
    print("It is not a palindrome")