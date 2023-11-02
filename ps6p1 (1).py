#input phase
qty = int(input("Enter quantity:  "))

#process phase
if qty > 10000:
    price = qty * 10
elif qty > 5000 or qty < 1000:
    price = qty * 20
  
else:
    price = qty * 30

#output phase
print("Extended price: ", price)
print("Tax amount: ", price * 0.07 )
print("Total price: ", (price + (price * 0.07)))
