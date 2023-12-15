def calcttp(chimiles):
  if chimiles >= 30:
      return 12
  elif 20 <= chimiles < 30:
      return 10
  elif 10 <= chimiles < 20:
      return 8
  else:
      return 5

def calcsttp():
  total = 0
  while True:
      print("\nDo you want to calculate the ticket price? (Yes or No)")
      response = input().lower()

      if response == 'yes':
        chimiles = float(input("Enter the miles from Chicago: "))
        ticket = calcttp(chimiles)
        total += ticket
        print("The ticket price is $", ticket, ".")
      elif response == 'no':
        break
      else:
        print("Enter Yes or No.")

      return total

def main():
  totalsttp = calcsttp()
  print("\nThe total price of all the tickets is $", totalsttp, ".")
