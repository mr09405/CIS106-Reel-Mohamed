#input phase 
partno = int(input("Enter the part number"))
qty = int(input("Enter the quantity"))
  
#process phase
if partno == 10 or partno == 55:
    unitprice = 1.00
elif partno == 90:
  unitprice = 2.00
elif partno == 70 or partno == 80:
  unitprice = 3.00
else:
  unitprice = 5.00
  
total = float(qty) * unitprice
  
#output phase
print("Part number:   ", partno)
print("Unit price:    ", price)
print("Total:         ", total)