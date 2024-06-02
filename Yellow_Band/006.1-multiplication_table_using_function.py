def multiplication_table(num):
    print("printing"+str(num)+"tables:")
    for i in range(1,13):
        value=num*i
        print(str(num)+"x"+str(i)+"="+str(value))
    print()
multiplication_table(8)
