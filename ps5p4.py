#input phase 
appname = input("Enter appliance name: ")
appprice = float(input("Enter appliance price: "))

#process phase 
if appprice > 1000:
  costwarr = 0.10 * appprice
else:
  costwarr = 0.05 * appprice
total = appprice + costwarr

#output phase 
print("Appliance name: ", appname)
print("Appliance price: ", appprice)
print("Cost of warranty: ", costwarr)
print("Total cost: ", total)