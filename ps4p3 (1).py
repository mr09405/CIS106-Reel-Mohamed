#input phase
totalmeal = float(input("Enter the total meal price"))

#process phase
tipfifteen = totalmeal * 0.15
tipeighteen = totalmeal * 0.18
tiptwenty = totalmeal * 0.20
totalwtipfifteen = totalmeal + tipfifteen
totalwtipeighteen = totalmeal + tipeighteen
totalwtiptwenty = totalmeal + tiptwenty

#output phase
print("With 15% Tip: ")
print("The tip for a 15% tip is $ ", tipfifteen)
print("The total meal with 15% tip is $ ", totalwtipfifteen)
print("With 18% Tip: ")
print("The tip for a 18% tip is $ ", tipeighteen)
print("The total meal with 18% tip is $ ", totalwtipeighteen)
print("With 20% Tip: ")
print("The tip for a 20% tip is $ ", tiptwenty)
print("The total meal with 20% tip is $ ", totalwtiptwenty)