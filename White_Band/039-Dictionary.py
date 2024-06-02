fruits={
    'apple':50,
    'banana':20,
    'orange':30,
    'papaya':10
}

apple_price=fruits['apple']
print("Apple costs:" ,apple_price)

fruits['mango']=15
print(fruits)

del fruits['apple']
print(fruits)