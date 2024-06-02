fruits=["apples","oranges","Banana"]
for fruit in fruits:
    string_size=0
    for alphabet in fruit:
        string_size+=1
    print("The name of the fruit: %s is has length %s" % (fruit,string_size))