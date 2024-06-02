def max_of_three():

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    max_num = max(num1, num2, num3)
    return max_num


print(f"The maximum of the three numbers is: {max_of_three()}")

