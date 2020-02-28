"""
Question 3
"""

clients = {
  "client1" : {
    "name" : "Ali",
    "address" : "No 101, Seri Isk",
    "oldReading" : 5000,
    "newReading" : 5500
  },
  "client2" : {
    "name" : "Mei",
    "address" : "No 202, Seri Isk",
    "oldReading" : 5000,
    "newReading" : 6500
  },
  "client3" : {
    "name" : "Siva",
    "address" : "No 303, Seri Isk",
    "oldReading" : 5000,
    "newReading" : 8000
  }
}
  
for x in clients:        
    waterUnit = clients[x]["newReading"] - clients[x]["oldReading"]
    print("water unit:", waterUnit)
    
    if (waterUnit > 2000):
        waterUnit -= 2000
        bill = waterUnit * 0.10 + 1000 * 0.07 + 1000 * 0.05
    elif(waterUnit > 1000):
        waterUnit -= 1000
        bill = waterUnit * 0.07 + 1000 * 0.05
    else:
        bill = waterUnit * 0.05
    
    print("bill:", bill)