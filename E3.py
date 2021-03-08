# Let’s do a small example. Let’s say I want to make a piece of code that
# converts from a numerical grade (1-100) to a letter grade (A, B, C, D, F).

grade = int(input("Enter your grade"))
if grade >= 90:
    print("You have an A")
elif grade >= 80:
    print("You have a B")
elif grade >= 70:
    print("You have a C")
elif grade >= 60:
    print("You have a D")
else:
    print("You have an F")