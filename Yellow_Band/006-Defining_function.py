def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"
def calculator():
    print("simple calculator")
    num1=int(input("enter number 1:"))
    num2=int(input("Enter number 2:"))
    op=input("enter operation(+,-,*,/) :")

    if op=="+":
        result=add(num1,num2)
    elif op=="-":
        result=subract(num1,num2)
    elif op=="*":
        result=multiplication(num1,num2)
    elif op=="/":
        result=division(num1,num2)
    else:
        print("Invalid operation")

    print("result: ",result)

calculator()