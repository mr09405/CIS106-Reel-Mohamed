f = open(sys.argv[1], "r")

c = 0
totaltuition = 0.0

#jkg

lname = str(f.readline().rstrip(",\n"))

while lname != "":
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())

  if dcode == "I":
    cpc = 250.00
else:
  cpc = 500.00

tuition = cpc * credits
c = c + 1
totaltuition = totaltuition + tuition

print("Student: ", lname)
print("Credits taken: ", credits)
print("Tuition Owed: ", tuition)

lname = str(f.readline().rstrip('\n'))

f.close()

print("Number of students: ", c)
print("Total tuition owed: ", totaltuition)
