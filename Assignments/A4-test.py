# Assignment 4
# The Candy Locker

# Named constant
BILL_CHOICE = 1
AVAILIBLE_CHOICE = 2
CONSUME_CHOICE = 3
PURCHASE_CHOICE = 4
QUIT_CHOICE = 5
NEW_STOCK = 15
NEW_STOCK_PRICE = 15
STOCK_PURCHASE = 10
STOCK_PURCHASE_PRICE = 11
AUTO_STOCK = 10
AUTO_STOCK_PRICE = 15

# Main program module
def main():
  choice = 0

  # probably need the while and if together...
  while choice != QUIT_CHOICE:
    # display menu
    getMenu()

    # get user's choice
    getChoice()

# user-input loop that gives a user 5 choices
def getMenu(x, y):
  print("Availible Bars: ", x)
  print("Cost (so far) this month: $", y)
  print("------------------------------------")
  print("Menu\tB: Show Bill and start new month")
  print("\tA: Show Availilbe number of bars for current Month")
  print("\tC: Consume bars now")
  print("\tP: Purchase additional bars for current month")
  print("\tQ: show bill and Quit")

def getChoice():
  B = BILL_CHOICE
  A = AVAILIBLE_CHOICE
  C = CONSUME_CHOICE
  P = PURCHASE_CHOICE
  Q = QUIT_CHOICE
  print('Please select B, A, C, or P to continue')
  print('or enter Q to view bill and quit')
  choice = str(input('please make selection')).upper()

  if choice == 'B':
    print('you choose B')
  elif choice == 'A':
    print('you choose A')
  elif choice == 'C':
    print('you choose C')
  elif choice == 'P':
    print('you choose P')
  else:
    print("Error: invalid selection.")
    getChoice()


main()
