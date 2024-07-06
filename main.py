import os

print('Welcome to the silent auction program.')

still_biding = True

def calculate_winner():
  winner_name = ''
  winner_bid = 0
  for name in dictionary:
    if(dictionary[name] > winner_bid):
      winner_bid = dictionary[name]
      winner_name = name
  print(f"The winner is {winner_name} with a bid of {winner_bid}")

dictionary = {}

while(still_biding):
  
  name = input('What is your name?: \n')
  bid = float(input("What is your bid?: \n$"))
  dictionary[name] = bid

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if(other_bidders == 'no'):
    calculate_winner()
    still_biding = False
  elif(other_bidders == 'yes'):
    os.system('clear')

