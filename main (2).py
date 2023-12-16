def dl1 (mylist):
  n = int(input("Number of items for your list: "))
  for n in range(0,n,1):
   s = int(input("Enter an integer: "))
   mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []
mylist = dl1(mylist)
print(mylist)

mylist.insert(0,99)
print(mylist)

mylist[0] = 100
print(mylist)

mylist2 = ["Mohamed", "Patrick", "Adams", "Brown"]
mylist3 = ["White", "Scott", "Anderson", "Neile"]
mylist2.extend(mylist3)
print(mylist)

mylist2.remove("Brown")
print(mylist2)

print("Count of Adams in the list", mylist2.count ("Adams"))
print("Scott position in the list ",mylist2.index ("Scott"))