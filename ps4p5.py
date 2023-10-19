#input phase
fixedcosts = float(input("Enter fixed costs: $"))
ppunit = float(input("Enter price per unit: $"))
cpunit = float(input("Enter cost per unit: $"))

#process phase 
breakevenpoint = fixedcosts / (ppunit-cpunit)

#output phase
print("Breakeven point:", breakevenpoint, "items")