#input phase 
ticketno = int(input("Enter number of concert tickets : "))

#processing phase
if ticketno >=25:
    priceperticket = 50
    cost = ticketno * priceperticket
  
elif ticketno <=24 and ticketno >= 10:
    priceperticket = 60
    cost = ticketno * priceperticket 

elif ticketno <=9 and ticketno >= 5:
    priceperticket = 70
    cost = ticketno * priceperticket

else:
  priceperticket = 75
  cost = ticketno * priceperticket
    
#output phase
print("The number of concert tickets is: ", ticketno)  
print("The price per ticket is: ", priceperticket)
print("The total cost is: ", cost)
