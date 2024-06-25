print("List of squares:")
number=[1,2,3,4,5,6]
squares=[num**2 for num in number]
print(squares)

print("______________________________________________________________________________________________________________")

print("Filtering even numbers:")
numbers=[1,2,3,4,5,6,7]
even_numbers=[num for num in numbers if num % 2==0]
print(even_numbers)

print("______________________________________________________________________________________________________________")

print("Convert string to uppercase")
words=["apple","banana","cherry"]
uppercase=[word.upper() for word in words]
print(uppercase)