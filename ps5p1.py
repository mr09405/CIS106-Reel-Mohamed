#input phase 
qty = float(input("Enter the quantity: "))

#process phase 
if qty >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00
extendedprice = qty * unitprice 
tax = extendedprice * 0.07
total = extendedprice + tax

#output phase 
print("The quantity is:  ", qty)
print("The unit price is:  ", unitprice)
print("The extended price is: ", extendedprice)
print("The tax is: ", tax)
print("The total is: ", total)