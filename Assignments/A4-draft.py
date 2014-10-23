# Assignment 4
# The Candy Locker

# Each month all candybar stock returns to 0
# --> then, new stock is added (15 bars for $15)
# --> bars can only be consumed 1-10 bars at a time
# ----> which is to say, it takes two sessions to consume 15 bars
# Two ways to consume--a less expensive way and a more expensive way
# Way 1--PLANED: buy before reaching 0 availible bars
# --> purchase 10 bars for $11
# ----> can only purchase 30 bars at once ($33), but can make infinite purcases
#       a month
# Way 2--> AUTOMATIC: consume negative bars that are purchased automatically
# --> automatic 10 bars for $15 (10 bars garuntees enough for one session)

# Global/named constants
# --> User choices are assigned numberic values
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
# global constants are assigned string letters for menu + validation
# local constant "choice" controls loop
# local constant "stock" + "bill" will collect totals until a new month is started
def main():
  choice = 0
  B = BILL_CHOICE
  A = AVAILIBLE_CHOICE
  C = CONSUME_CHOICE
  P = PURCHASE_CHOICE
  Q = QUIT_CHOICE
  stockSum = 15
  billSum = 15
  newStock, newBill = newBill(stockSum, billSum)
  consumeStock, consumeBill = consume(stockSum, billSum)
  purchaseStock, purchaseBill = purchase(stockSum, billSum)
  stockSum = newStock + consumeStock + purchaseStock
  billSum = newBill + consumeBill + purchaseBill


  # Menu displayed through function
  # if/elif/else loop to validate user choice and call other functions called
  while choice != 'Q':
    # display menu
    getMenu(stockSum, billSum)

    # get user's choice as string
    # --> input validated through the while loop and .upper() to convert input
    print('\nPlease select B, A, C, or P to continue')
    print('or enter Q to view bill and quit')
    choice = str(input('please make selection')).upper()

    # if/elif/else loop for user choice
    if choice == 'B':
      print('you choose B')
      newBill(stockSum, billSum)
    elif choice == 'A':
      print('you choose A')
      availibleNow(stockSum)
    elif choice == 'C':
      print('you choose C')
      consume(stockSum, billSum)
    elif choice == 'P':
      print('you choose P')
      purchase(stockSum, billSum)
    elif choice == 'Q':
      print("you've chosed to quit")
      quit(stockSum, billSum, choice)
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
def newBill(nst, nbll):
	# where variable nst = new stock amount
	# where variable nbll = new stock bill
  nst = NEW_STOCK
  nbll = NEW_STOCK_PRICE

  # return the modified nst/nbll variables to main()
  return nst, nbll

# Option A function--show availible capacity for current month
# --> show availible bars but do nothing
def availibleNow(nst):
  print('you have', nst, 'bars left')

  # return the nst variable to main()
  return nst


# Option C function--consume bars now
# --> ask how many bars to consume (1-10)
# --> subtract from availilbe capacity
# --> if consume more than capacity--make auto purchase
def consume(cst, cbll):
  # cst / stock decreses by the number user enters to eat
  # cbill / bill increases if user eats more than the remainder of cst
  # eat controls loop
  eat = 'n'

  while eat != 0:
    print('\nSo, how many bars would you like to eat?')
    print('Note: you can only eat 1-10 bars at a time!')
    eat = int(input('Enter number: '))

    # conditions to eat one bar
    if eat == 1 and cst >= 1:
      cst = cst - 1
      eat = 0
    elif eat == 1 and cst <= 1:
      stock = cst + AUTO_STOCK - 1
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat two bars
    elif eat == 2 and cst >= 2:
      cst = cst - 2
      eat = 0
    elif eat == 2 and cst <= 2:
      stock = cst + AUTO_STOCK - 2
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat three bars
    elif eat == 3 and cst >= 3:
      cst = cst - 3
      eat = 0
    elif eat == 3 and cst <= 3:
      stock = cst + AUTO_STOCK - 3
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat four bars
    elif eat == 4 and cst >= 4:
      cst = cst - 4
      eat = 0
    elif eat == 4 and cst <= 4:
      stock = cst + AUTO_STOCK - 4
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat five bars
    elif eat == 5 and cst >= 5:
      cst = cst - 5
      eat = 0
    elif eat == 5 and cst <= 5:
      stock = cst + AUTO_STOCK - 5
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat six bars
    elif eat == 6 and cst >= 6:
      cst = cst - 6
      eat = 0
    elif cst <= 6 and cst <= 6:
      stock = cst + AUTO_STOCK - 6
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat seven bars
    elif eat == 7 and cst >= 7:
      cst = cst - 7
      eat = 0
    elif eat == 7 and cst <= 7:
      stock = cst + AUTO_STOCK - 7
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat eight bars
    elif eat == 8 and cst >= 8:
      cst = cst - 8
      eat = 0
    elif cst <= 8:
      stock = cst + AUTO_STOCK - 8
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat nine bars
    elif eat == 9 and cst >= 9:
      cst = cst - 9
      eat = 0
    elif eat == 9 and cst <= 9:
      stock = cst + AUTO_STOCK - 9
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat ten bars
    elif eat == 10 and cst >= 10:
      cst = cst - 10
      eat = 0
    elif eat == cst <= 10:
      stock = cst + AUTO_STOCK - 10
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0

    # conditions to eat zero bars
    elif eat == 0:
      cst == cst
      print('lost your appetite? :P')
    else:
      print('Error; please enter a whole number between 1-10; or, 0 to quit')

  return cst, cbll


# Option P function--purchase additional bars
# --> purchase 1-3 sets of 10 bars
# --> add to bill and capacity
def purchase(pst, pbll):
  # pst / stock increases by 10 when 1 set is purchased
  # pbll / bill is increased by 11 each time 1 set is purchased
  # buy controls loop
  buy = 'n'

  while buy != 0:
    print('\nSo, how many sets of bars would you like to buy?')
    print('Note: you can only buy 1-3 sets of 10 bars at a time!\
          \nAlso, 1 set of 10 costs $11')
    buy = int(input('Enter number: '))

    if buy == 1:
      pst = pst + STOCK_PURCHASE
      pbll = pbll + STOCK_PURCHASE_PRICE
    elif buy == 2:
      pst = pst + (STOCK_PURCHASE * 2)
      pbll = pbll + (STOCK_PURCHASE_PRICE * 2)
    elif buy == 3:
      pst = pst + (STOCK_PURCHASE * 3)
      pbll = pbll + (STOCK_PURCHASE_PRICE * 3)
    elif buy == 0:
      pbll = pbll
    else:
      print('Error; please enter a whole number between 1-3; or, 0 to quit')

    # return pst + pbll for use in main()
    return pst, pbll


# Option Q--show final bill and quit
# --> show total bill (don't show capacity)
# --> quit loop
def quit(stsum, bllsum, choi):
  choi = Q
  print("You have donated all", stsum, "bars to charity")
  print("You owe: $", bllsum, "\nplease pay with BitCoin.")

  print('.')
  print('.')
  print('.')
  print('.')
  stsum = 0
  bllsum = 0
  print("You now have", stsum, "bars, and now owe, $", billSum)

  # return stsum/bllsum variables and the 'Q' for quit variable to main()
  return stsum, bllsum, choice


# call the main function
main()
