#input phase 
qty = float(input( "Enter the quantity of books: "))
cost = float(input("Enter cost per book: $ "))

#process phase 
total = qty * cost 
if total > 50:
  sc = 0.00
else:
  sc = 25.00
ep = total + sc

#output phase 
print("The total cost of the books is: $", ep)
print("The shipping charge is: $", sc)