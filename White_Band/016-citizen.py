age=int(input("Enter your age:"))
if age<0:
    print("It is invalid number,please enter proper number")
elif age<18:
    print("You are minor")
elif age<65:
    print('you are an adult')
else:
    print("you are senior citizen")