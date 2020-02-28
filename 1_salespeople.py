"""
Question 1
"""

# every salespeople weekly sales
weeklySales = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
# salary or commision category from 200-299 until >1000
category = [0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range( len(weeklySales) ):
    #salary = 200 basic + 9% of weekly sales
    salary = 200 + 0.09 * weeklySales[i]
    print(int(salary))
    
    if (salary >= 1000):
        category[8]+=1
    elif (salary >= 900):
        category[7]+=1
    elif (salary >= 800):
        category[6]+=1
    elif (salary >= 700):
        category[5]+=1
    elif (salary >= 600):
        category[4]+=1
    elif (salary >= 500):
        category[3]+=1
    elif (salary >= 400):
        category[2]+=1
    elif (salary >= 300):
        category[1]+=1
    elif (salary >= 200):
        category[0]+=1
        
    print(category)

print("\nSalespeople in salary range:")

for i in range(len(category) - 1):
    startNum = 200 + 100 * i
    endNum = 299 + 100 * i
    print(startNum, "-", endNum, "=", category[i])

print("More then 1000 =", category[i])