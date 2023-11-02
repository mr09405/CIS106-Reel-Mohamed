#input phase 
lname = input("Enter last name:")
salary = float(input("Enter salary:"))
joblvl = int(input("Enter job level:"))
  
#processing phase
if joblvl == 10:
  bonusr = 0.25
  bonus = salary * bonusr
  
elif joblvl == 9 and joblvl >=5:
  bonusr = 0.20
  bonus = salary * bonusr

else:
  bonusr = 0.10
  bonus = salary * bonusr
  
#output phase
print("Last name:", lname)
print("Bonus:", bonus)