my_list = [1, 2, 3, 4, 5]
my_list.append(6)
another_list = [7, 8, 9]
my_list.extend(another_list)
my_list.insert(2, 10) 
my_list.remove(3) 
popped_element = my_list.pop(4)  
index_of_4 = my_list.index(4)
count_of_2 = my_list.count(2)
my_list.reverse()
my_list.sort()
copied_list = my_list.copy()
for item in my_list:
    print(item, end=' ')
print()
for index, item in enumerate(my_list):
    print(f"Index: {index}, Value: {item}")
while my_list:
    print(my_list.pop(), end=' ')
print()
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in my_list if x % 2 == 0]
strings = ["hello", "world"]
uppercase_strings = [string.upper() for string in strings]
print("Modified list:", my_list)
print("Popped element:", popped_element)
print("Index of 4:", index_of_4)
print("Count of 2:", count_of_2)
print("Copied list:", copied_list)
print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Uppercase strings:", uppercase_strings)
