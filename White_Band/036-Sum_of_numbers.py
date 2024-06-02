total=0
user_ip=input("enter the number (type 'Stop' to an end):")
while user_ip.lower()!="stop":
    total+=int(user_ip)
    user_ip = input("enter the number (type 'Stop' to an end):")
print("sum of numbers:",total)