#input phase
firstexamscore = float(input("Enter the your first exam score"))
secondexamscore = float(input("Enter the your second exam score"))

#process phase
firstexamscorew = firstexamscore * 0.60
secondexamscorew = secondexamscore * 0.40 
totalexamscore = firstexamscorew + secondexamscorew

#output phase 
print("Your total exam score is:", totalexamscore)