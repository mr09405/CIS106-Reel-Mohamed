#input phase 
principle = float(input("Enter the principle amount: "))
ytm = int(input("Enter the years to maturity: "))

#processing phase 
if principle > 100000:
  if ytm >= 5:
    interest = 0.06
elif 5000 <= principle <= 100000:
  if ytm == 10:
    interest = 0.05
  elif ytm == 5:
    interest = 0.04
else:
    interest = 0.02

finalint = principle * interest

#output phase 
print("The principle amount is: ", principle)
print("The interest rate is: ", interest)
print("The final interest amount for the first year is: ", finalint)