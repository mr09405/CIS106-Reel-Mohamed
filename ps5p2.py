#input phase
item = input("Enter item A or B: ")
qty = float(input("Enter qunatity:  "))

#process phase
if item == "A":
  up = 10.00
elif item == "B":
  up = 20.00
extprice = qty * up

#output phase
print("Item: ", item)
print("Unit Price: $ ", up)
print("Extended price: ", extprice)