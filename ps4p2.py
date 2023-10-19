#input phase 
ppshare = float(input("Enter the price per share: "))
currentstockprice = float(input( "Enter the current stock price: "))
qtystock = float(input( "Enter the quantity of stock: "))
#process phase
value = (currentstockprice - ppshare) * qtystock
#output phase
print("The value of the stock  is: ", value)