counter = 0
sum = 0

#input phase 
Response = input("Would you like to participate in this program? Yes or No ")

#proccess phase 

while Response == "Yes":
  counter = counter + 1
  lname = input("Enter last name: ")
  hours = float(input("Enter hours worked: "))
  pay = float(input("Enter pay rate: "))
  if hours >= 40:
    gross = (40 * pay) + ((hours - 40) * pay * 1.5) 
  else:
    gross = hours * pay

  print ("Last name: $ ", lname)
  print ("Gross pay: $ ", gross)
  sum = sum + gross
  Response = input("Would you like to participate in this program? Yes or No ")

#output phase 
avggrosspay = sum / counter 
print ("Sum of all gross pay is: $ ", sum)
print ("Number of employees: ", counter)
print ("Average gross pay is: $ ", avggrosspay)