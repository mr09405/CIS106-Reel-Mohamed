#input phase 
make = input("Enter vehicle make:")
model = input("Enter vehicle model:")
msrpamnt = float(input("Enter MSRP amount:$"))
discprcnt = float(input("Enter discount percent:"))

#process phase 
amntoffmsrp = msrpamnt * discprcnt
discprice = msrpamnt - amntoffmsrp
discprcnt = discprcnt

#output phase 
print("The make of the vehicle is ", make)
print("The model of the vehicle is ", model)
print("The MSRP of the vehicle is ", msrpamnt)
print("The discount percent of the vehicle is ", discprcnt)
print("The amount off MSRP of the vehicle is $", amntoffmsrp)
print("The discounted price of the vehicle is $ ", discprice)