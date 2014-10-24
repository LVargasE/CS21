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

def main():
  choice = 0
  B = BILL_CHOICE
  A = AVAILIBLE_CHOICE
  C = CONSUME_CHOICE
  P = PURCHASE_CHOICE
  Q = QUIT_CHOICE
  stockSum = NEW_STOCK
  billSum = NEW_STOCK_PRICE
  getNewStock = NEW_STOCK
  getNewBill = NEW_STOCK_PRICE
  getNewStock, getNewBill = newBill(stockSum, billSum)
  consumeStock = 0
  consumeBill = 0
  consumeStock, consumeBill = consume(stockSum, billSum)
  purchaseStock = 0
  purchaseBill = 0
  purchaseStock, purchaseBill = purchase(stockSum, billSum)
  stockSum = getNewStock + consumeStock + purchaseStock
  billSum = getNewBill + consumeBill + purchaseBill
  while choice != 'Q':
    getMenu(stockSum, billSum)
    print('\nPlease select B, A, C, or P to continue')
    print('or enter Q to view bill and quit')
    choice = str(input('please make selection')).upper()
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
  print("Thank you!  Have a nice day!")

def getMenu(x, y):
  print("Availible Bars: ", x)
  print("Cost (so far) this month: $", y)
  print("Menu\tB: Show Bill and start new month")
  print("\tA: Show Availilbe number of bars for current Month")
  print("\tC: Consume bars now")
  print("\tP: Purchase additional bars for current month")
  print("\tQ: show bill and Quit")

def newBill(nst, nbll):
  nst = NEW_STOCK
  nbll = NEW_STOCK_PRICE
  return nst, nbll

def availibleNow(nst):
  print('you have', nst, 'bars left')
  return nst

def consume(cst, cbll):
  eat = 'n'
  while eat != 0:
    print('\nSo, how many bars would you like to eat?')
    print('Note: you can only eat 1-10 bars at a time!')
    eat = int(input('Enter number: '))
    if eat == 1 and cst >= 1:
      cst = cst - 1
      eat = 0
    elif eat == 1 and cst <= 1:
      stock = cst + AUTO_STOCK - 1
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 2 and cst >= 2:
      cst = cst - 2
      eat = 0
    elif eat == 2 and cst <= 2:
      stock = cst + AUTO_STOCK - 2
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 3 and cst >= 3:
      cst = cst - 3
      eat = 0
    elif eat == 3 and cst <= 3:
      stock = cst + AUTO_STOCK - 3
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 4 and cst >= 4:
      cst = cst - 4
      eat = 0
    elif eat == 4 and cst <= 4:
      stock = cst + AUTO_STOCK - 4
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 5 and cst >= 5:
      cst = cst - 5
      eat = 0
    elif eat == 5 and cst <= 5:
      stock = cst + AUTO_STOCK - 5
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 6 and cst >= 6:
      cst = cst - 6
      eat = 0
    elif cst <= 6 and cst <= 6:
      stock = cst + AUTO_STOCK - 6
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 7 and cst >= 7:
      cst = cst - 7
      eat = 0
    elif eat == 7 and cst <= 7:
      stock = cst + AUTO_STOCK - 7
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 8 and cst >= 8:
      cst = cst - 8
      eat = 0
    elif cst <= 8:
      stock = cst + AUTO_STOCK - 8
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 9 and cst >= 9:
      cst = cst - 9
      eat = 0
    elif eat == 9 and cst <= 9:
      stock = cst + AUTO_STOCK - 9
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 10 and cst >= 10:
      cst = cst - 10
      eat = 0
    elif eat == cst <= 10:
      stock = cst + AUTO_STOCK - 10
      cbll = cbll + AUTO_STOCK_PRICE
      eat = 0
    elif eat == 0:
      cst == cst
      print('lost your appetite? :P')
    else:
      print('Error; please enter a whole number between 1-10; or, 0 to quit')
  return cst, cbll

def purchase(pst, pbll):
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
    return pst, pbll

def quit(stsum, bllsum, choi):
  choi = 'Q'
  print("You have donated all", stsum, "bars to charity")
  print("You owe: $", bllsum, "\nplease pay with BitCoin.")
  stsum = 0
  bllsum = 0
  print("You now have", stsum, "bars, and now owe, $", billSum)

main()
