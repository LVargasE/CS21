# Assignment 4
# The Candy Locker

# Each month all candybar stock returns to 0
# --> then, new stock is added (15 bars for $15)
# --> bars can only be consumed 1-10 bars at a time
# ----> which is to say, it takes two sessions to consume 15 bars
# Two ways to consume--a less expensive way and a more expensive way
# Way 1--PLANED: buy before reaching 0 availible bars
# --> purchase 10 bars for $11
# ----> can only purchase 30 bars at once ($33), but can make infinite purcases a month
# Way 2--> AUTOMATIC: consume negative bars that are purchased automatically
# --> automatic 10 bars for $15 (10 bars garuntees enough for one session)

# Named constants
# --> Choices are assigned numberic values
# --> Stock numbers and price numbers assigned to ease use of computation
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
# global constants are assigned string letters for menu options
# local constant choice controls loop
# local constant stock and bill will collect totals until a new month is started
def main():
  choice = 0
  B = BILL_CHOICE
  A = AVAILIBLE_CHOICE
  C = CONSUME_CHOICE
  P = PURCHASE_CHOICE
  Q = QUIT_CHOICE
  stock = 0
  bill = 0
  newStock, newBill = newBill(stock, bill)
  consumeStock, consumeBill = consume(st, bll)
  purchaseStock, purchaseBill =



  # Menu displayed through function
  # if/elif/else loop to validate user choice and call other functions called
  while choice != 'Q':
    # display menu
    getMenu(availibleBars, currentBill)

    # get user's choice as string
    # --> input validated through the while loop and .upper() to convert input
    print('\nPlease select B, A, C, or P to continue')
    print('or enter Q to view bill and quit')
    choice = str(input('please make selection')).upper()

    # if/elif/else loop for user choice
    if choice == 'B':
      print('you choose B')
    elif choice == 'A':
      print('you choose A')
    elif choice == 'C':
      print('you choose C')
      consume(stock, bills)
    elif choice == 'P':
      print('you choose P')

    elif choice == 'Q':
      print('you've chosed to quit)
      ?quit()
    else:
      print("Error: invalid selection.")

  # exit loop
  print("Thank you!  Have a nice day!")



# Menu function
# --> user-input loop that gives a user 5 choices
# --> variables will pass through the function as arguments
def getMenu(x, y):
	# x = number of availible bars, y = current bill
  print("Availible Bars: ", x)
  print("Cost (so far) this month: $", y)
  print("------------------------------------")
  print("Menu\tB: Show Bill and start new month")
  print("\tA: Show Availilbe number of bars for current Month")
  print("\tC: Consume bars now")
  print("\tP: Purchase additional bars for current month")
  print("\tQ: show bill and Quit")



# Option B function--show bill and start a new month
# --> close month
# --> display what they owe for that month
# --> display bars that are lost/unconsumed
# --> reset availible capacity to 15 bars with a $15 tab
def newBill(st, pr):
	# where variable st = new stock amount
	# where variable pr = new stock price
  st = NEW_STOCK
  pr = NEW_STOCK_PRICE

  return st, pr

# Option A function--show availible capacity for current month
# --> show availible bars but do nothing
def availibleNow(availible):
  print('you have', availible, 'bars left')


# Option C function--consume bars now
# --> ask how many bars to consume (1-10)
# --> subtract from availilbe capacity
# --> if consume more than capacity--make auto purchase
def consume(st, bll):
  # consume st / stock and add to bll / bill if stock is too low
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


# Option P function--purchase additional bars
# --> purchase 1-3 sets of 10 bars
# --> add to bill and capacity
def purchase():
  buy = 'n'

  while buy != 0:
    print('\nSo, how many sets of bars would you like to buy?')
    print('Note: you can only buy 1-3 sets of 10 bars at a time!\
          \nAlso, 1 set of 10 costs $11')
    buy = int(input('Enter number: '))

    if buy == 1:
      stock = stock + STOCK_PURCHASE_PRICE
    elif buy == 2:
      stock = stock + (STOCK_PURCHASE_PRICE * 2)
    elif buy == 3:
      stock = sotck + (STOCK_PURCHASE_PRICE * 3)
    elif buy == 0:
      stock = stock
    else:
      print('Error; please enter a whole number between 1-3; or, 0 to quit')


# Option Q--show final bill and quit
# --> show total bill (don't show capacity)
# --> quit loop
def quit():
	choice = Q
	return Q

# call the main function
main()
