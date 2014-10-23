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
  billSum = NEW_STOCK_BILL
  newStock = NEW_STOCK
  newBill = NEW_STOCK_BILL
  newStock, newBill = newBill(stockSum, billSum)
  consume = 0
  consumeStock, consumeBill = consume(stockSum, billSum)
  purchase = 0
  purchaseStock, purchaseBill = purchase(stockSum, billSum)
  stockSum = newStock + consumeStock + purchaseStock
  billSum = newBill + consumeBill + purchaseBill
  while choice != 'Q':
    getMenu(stockSum, billSum)
    print('\nPlease select B, A, C, P, or Q to quit')
    choice = str(input('please make selection')).upper()
    if choice == 'B':
      newBill(stockSum, billSum)
    elif choice == 'A':
      availibleNow(stockSum)
    elif choice == 'C':
      consume(stockSum, billSum)
    elif choice == 'P':
      purchase(stockSum, billSum)
    elif choice == 'Q':
      quit(stockSum, billSum, choice)
    else:
      print("Error: invalid selection.")

def getMenu(x, y):
  print("Availible Bars: ", x, "cost = $", y)
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
    eat = int(input('Enter number: '))
    if eat == 1 and cst >= 1:
      cst = cst - 1
      eat = 0
    elif eat == 1 and cst <= 1:
      stock = cst + AUTO_STOCK - 1
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
    buy = int(input('Enter number: '))
    if buy == 1:
      pst = pst + STOCK_PURCHASE
      pbll = pbll + STOCK_PURCHASE_PRICE
    elif buy == 0:
      pbll = pbll
    else:
      print('Error; please enter a whole number between 1-3; or, 0 to quit')
    return pst, pbll

def quit(stsum, bllsum, choi):
  choi = Q
  print("You have donated all", stsum, "bars to charity + owe $", bllsum)
  stsum = 0
  bllsum = 0
  print("You now have", stsum, "bars, and now owe, $", billSum)
  return stsum, bllsum, choice
main()
