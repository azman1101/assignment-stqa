"""
Question 2
"""

# list/array of distinct number
distinctNumber = []
# condition of new input number
isItDistinct = True

for _ in range(10):
    num = input("Enter a number: ")
    
    # initialize condition
    isItDistinct = True
    
    # num is compare one by one with distinctNumber
    for i in range( len(distinctNumber) ):
        if (num == distinctNumber[i]):
            isItDistinct = False
            # if same number already exist, condition will be False, so num will not be append in distinctNumber
            # simple way, isItDistinct? Yes or No?
    
    # if it is distinct, then add num into the list/array
    if (isItDistinct == True):
        distinctNumber.append(num)
        
    print(distinctNumber)
