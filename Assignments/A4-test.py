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
  B = BILL_CHOICE
  A = AVAILIBLE_CHOICE
  C = CONSUME_CHOICE
  P = PURCHASE_CHOICE
  Q = QUIT_CHOICE



  # probably need the while and if together...
  while choice != 'Q':
    # display menu
    getMenu()

    # get user's choice
    print('\nPlease select B, A, C, or P to continue')
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
    elif choice == 'Q':
      print('you quit')
      choice == QUIT_CHOICE
    else:
      print("Error: invalid selection.")

  # exit
  # will need some kind of exit() module
  print("you're a quitter!")

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

def consume(st, bll):
  """consume st / stock and add to bll / bill if stock is too low"""
  eat = 'n'

  while eat != 0:
    print('\nSo, how many bars would you like to eat?')
    print('Note: you can only eat 1-10 bars at a time!')
    eat = int(input('Enter number: '))

    if eat == 1 and st >= 1:
      st = st - 1
      eat = 0
    elif eat == 1 and st <= 1:
      stock = st + AUTO_STOCK - 1
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 2 and st >= 2:
      st = st - 2
      eat = 0
    elif eat == 2 and st <= 2:
      stock = st + AUTO_STOCK - 2
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 3 and st >= 3:
      if st >= 3:
      st = st - 3
      eat = 0
    elif eat == 3 and st <= 3:
      stock = st + AUTO_STOCK - 3
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 4 and st >= 4:
      st = st - 4
      eat = 0
    elif eat == 4 and st <= 4:
      stock = st + AUTO_STOCK - 4
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 5 and st >= 5:
      st = st - 5
      eat = 0
    elif eat == 5 and st <= 5:
      stock = st + AUTO_STOCK - 5
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 6 and st >= 6:
      st = st - 6
      eat = 0
    elif st <= 6 and st <= 6:
      stock = st + AUTO_STOCK - 6
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 7 and st >= 7:
      st = st - 7
      eat = 0
    elif eat == 7 and st <= 7:
      stock = st + AUTO_STOCK - 7
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 8 and st >= 8:
      st = st - 8
      eat = 0
    elif st <= 8:
      stock = st + AUTO_STOCK - 8
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 9 and st >= 9:
      st = st - 9
      eat = 0
    elif eat == 9 and st <= 9:
      stock = st + AUTO_STOCK - 9
      bll = bll + AUTO_STOCK_PRICE
      eat = 0
      ds
    elif eat == 10 and st >= 10:
      st = st - 10
      eat = 0
    elif eat == st <= 10:
      stock = st + AUTO_STOCK - 10
      bll = bll + AUTO_STOCK_PRICE
      eat = 0

    elif eat == 0:
      st == st
      print('lost your appetite? :P')
    else:
      print('Error; please enter a whole number between 1-10; or, 0 to quit')
  return st, bll

main()
