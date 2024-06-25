#string as a list:
print("Iterate through character in string:")
sentence="Welcome to AspHero"
for i in sentence:
    print(i)
print("__________________________________________________________________________________________________________")
#Accessing character by index

print("Accessing character by index")
print("first_letter: ",sentence[0])

#Slicing a String
print("Slicing a String")
print(sentence[11:])
print("__________________________________________________________________________________________________________")
#Reversing a String
print("Reversing a String:")
print(sentence[::-1])
print("__________________________________________________________________________________________________________")

#Checking if a String is Palindrome:
word="radar"
if word==word[::-1]:
    print(word,"is palindrome")
print("__________________________________________________________________________________________________________")

#Converting String to List of Characters
print(list(word))
print("__________________________________________________________________________________________________________")

#Counting Occurrences of a Character:
print("Counting Occurrences of a Character")
print(sentence.count('e'))

#Replacing Characters in a String
print("Replacing Characters in a String:")
a=sentence.replace('AspHero','DBB')
print(a)

#Joining Characters from a List into a String:
print("Joining Characters from a List into a String")
character=['p','y','t','h','o','n']
print(''.join(character))

#Splitting a String into a List
print("Splitting a String into a List:")
sentences="Welcome to DBB"
print(sentences.split())

#Checking if String Starts/Ends with a Substring
print("Checking if String Starts/Ends with a Substring")
word="python"
print(word.startswith("py"))
print(word.endswith("hon"))