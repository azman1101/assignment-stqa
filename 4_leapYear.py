"""
Question 4
"""

year = input("Enter a year number:")

if ( int(year) % 400 == 0 ):
    print("It's a leap year")
elif ( int(year) % 100 == 0  ):
    print("Not leap year")
elif ( int(year) % 4  == 0 ):
    print("It's a leap year")
else:
    print("Not leap year")