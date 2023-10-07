#input phase
stocktickersymbol = input("Enter stock ticker symbol")
numbershares = float(input("Enter number of shares"))
costpershare = float(input("Enter cost per share"))

#process phase
amntinvested = numbershares * costpershare

#output phase
print("Stock ticker symbol: ", stocktickersymbol)
print("Amount invested: $ ", amntinvested)
