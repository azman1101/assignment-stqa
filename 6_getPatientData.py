"""
Question 6
"""
# variable declaration
patient = {
        "name" : "",
        "IC" : "",
        "admission" : 0
        }

dailyRate = 50

daySpent = -1
medCharge = -1
hospServCharge = -1

def getPatientData():
    global patient
    
    patient["name"] = input("Enter patient name: ")
    patient["IC"] = input("Enter patient IC: ")
    
    print("\nPlease choose patient admission type:")
    print("1. In-patient")
    print("2. Out-patient")
    patient["admission"] = input("\nAdmission type:")

    return patient["admission"]

def calculateInPatientCharges(daySpent):
    global medCharge, hospServCharge
    total = dailyRate * daySpent + medCharge + hospServCharge
    return total

def calculateOutPatientCharges():    
    global medCharge, hospServCharge
    total = medCharge + hospServCharge
    return total

# main function start here
admissionType = int( getPatientData() )

    # if In-patient
if (admissionType == 1):
    while (daySpent < 0):
        daySpent = int(input("How many day spent: "))

while (medCharge < 0):
    medCharge = int(input("Hospital medication charges: "))

while (hospServCharge < 0):
    hospServCharge = int(input("Charges for hospital services (lab test, etc): "))

if (admissionType == 1):
    totalFee = calculateInPatientCharges(daySpent)
elif (admissionType == 2):
    totalFee = calculateOutPatientCharges()

print("\nName:", patient["name"])
print("IC  :", patient["IC"])
print("Total charge is RM", totalFee)
# main function end here
