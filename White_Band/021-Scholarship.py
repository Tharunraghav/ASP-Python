print("This is Central government Scheme Enter your Details:")
salary=int(input("Enter your salary:"));
fam_members=int(input("Enter number of persons in your family:"))
state=input("Enter your state");
state=state.lower()
if salary < 50000 and fam_members <= 4 and (state=="tamilnadu" or state=="kerala"):
    print("you are eligible for the central government scheme")
else:
    print("sorry you are above the poverty level")
