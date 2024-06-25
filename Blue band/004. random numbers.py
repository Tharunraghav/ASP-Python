import random
#random float
random_float=random.random()
print("Random Float : ",random_float)

#random integer
random_int=random.randint(1,6)
print("RandomInteger :",random_int)

#random float in range
random_float_u=random.uniform(1.5,3.0)
print("Random_float_uniform: ",random_float_u)

#randrange
a=random.randrange(0,50,10)
print("random range:",a)

#Choice(seq)

fruits=['apple','banana','orange','strawberry']
print("random fruit : ",random.choice(fruits))

#sample (population,k)
number=[1,2,3,4,5,6,7,8,9]
print("Random sample:",random.sample(number,3))

#shuffle

cards=['Ace','2','3','4','5','6','7','8','9','J','Q','k']
random.shuffle(cards)
print("Shuffled Cards:",cards)

#seed
random.seed(42)
