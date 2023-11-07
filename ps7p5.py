#input phase 
Response = input("Would you like to participate in this program? Yes or No ")

#proccess phase 
sum = 0

while Response == "Yes":
  qty = float(input("Enter a quantity: "))
  price = float(input("Enter a price: "))
  extprice = qty * price 
  discount = extprice * .25 if extprice > 10000.00 else extprice * .10 
  total = extprice - discount
  sum = sum + discount 
  
  print ("Extended price: $ ", extprice)
  print ("Discount: $ ", discount)
  print ("Total: $ ", total)
  
  Response = input("Would you like to participate in this program? Yes or No ")

#output phase 
print ("Sum of discount: $ ", sum)