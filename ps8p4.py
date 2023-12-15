c = 0.0
totp_ex = 0.0

item = str(input("Enter item: "))

while item !="":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))

  ep = qty * price

  totp_ex = totp_ex + ep
  c = c + 1

  print("Item is:    ", item)
  print("Quantity is:    ", qty)
  print("Price is:    ", price)
  print("Extended Price is:   ", ep)


print("Total Extended Prices:   ", totp_ex)
print("Number of Orders:   ", c)
avg = totp_ex / c
print("Average  Order:     ", avg)