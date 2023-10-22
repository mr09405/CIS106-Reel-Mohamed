#input phase 
lname = input("Enter your last name: ")
numdep = float(input("Enter number of dependents: "))
grossinc = float(input("Enter gross income:  $ "))

#process phase 
adjgrossinc = grossinc - numdep * 12000
if grossinc > 5000:
    taxrate = 0.20
else:
    taxrate = 0.10
inctax = adjgrossinc * taxrate
if inctax < 0: 
    inctax = 100
    
#output phase
print("Last name: ", lname)
print("Gross Income:   $ ", grossinc)
print("Number of Dependents: ", numdep)
print("Adjusted gross income is: ", adjgrossinc)
print("Income tax is: ", inctax)
