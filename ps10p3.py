def carprice(msrp, make, model, evhcode):
  tax = 0.07
discp = 0.02 if evhcode == "Y" else 0

msrps = msrp * (1 - discp)
total = msrps * (1 + tax)

return total    

def calcsales(make, model, msrp, total):
  sales = {
    "make": make,
    "model": model,
    "msrp": msrp,
    "total": total
  }

  return sales

def print():
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  msrp = float(input("Enter the msrp of the car: "))
  evhcode = input("Is the car electric (Yes or No)?")

  ttl = carprice (msrp, make, model, evcode)
  sales = calcsales(make, model, msrp, total)
  return sales

while True:
  print("Do you want to calculate car price? (Yes or No)?")
 response == input().lower()
if response == 'yes':
  sales = calcsales()
  print("The total is, sales["make"], "is", sales["model"], "is", sales[total]")
  else response == 'no'
