number_of_days={
    'january':31,
    'february':28,
    'march':31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'November':30,
    'december':31
}
month=input("enter month:")
month=month.lower()

if month in number_of_days:
    answer=month.title()+" has "+str(number_of_days[month])+" days"
    print(answer)
else:
    print("Try entering valid month name")