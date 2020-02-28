"""
Question 5
"""

year = input("Enter car model year: ")
weight = input("Enter car weight: ")

year = int(year)
weight = int(weight)

#year = 1979
#weight = 2699

weightClass = 0
registrationFee = 0.0

if (year <= 1970):
    
    if (weight < 2700):
        weightClass = 1
        registrationFee = 16.50
    elif (weight <= 3800):
        weightClass = 2
        registrationFee = 25.50
    else:
        weightClass = 3
        registrationFee = 46.50

elif ( year < 1980):
    
    if (weight < 2700):
        weightClass = 4
        registrationFee = 27.00
    elif (weight <= 3800):
        weightClass = 5
        registrationFee = 30.50
    else:
        weightClass = 6
        registrationFee = 52.50
        
else:
    if (weight < 3500):
        weightClass = 7
        registrationFee = 19.50
    else:
        weightClass = 8
        registrationFee = 52.50
        
print("\nCar weight class:", weightClass)
print("Registration fee: RM", registrationFee)