age=int(input("How old are you:"))
borninindia=input("Are you born in India:")
residence=int(input('How many years of residence do you have:'))
eligiblity=True
if age<35:
    eligiblity=False;
if borninindia =="no":
    eligiblity=False
if residence<10:
    eligiblity=False

if eligiblity:
    print("You are Eligible for president")
else:
    print("You are not eligible for president")
