# Assignment 4
# The candy locker

# Each month all candybar stock returns to 0
# --> then, new stock is added (15 bars for $15)
# --> bars can only be consumed 1-10 bars at a time
# ----> which is to say, it takes two sessions to consume 15 bars
# Two ways to consume--a less expensive way and a more expensive way
# Way 1--PLANED: buy before reaching 0 availible bars
# --> purchase 10 bars for $11
# ----> can only purchase 30 bars at once ($33), but can make infinite purcases a month# Named constantSTOCK_PURCHASE = 10STOCK_PURCHASE_PRICE = 11
# Way 2--AUTOMATIC: consume negative bars that are purchased automatically
# --> automatic 10 bars for $15 (10 bars garuntees enough for one session)
# Named Constants
NEW_STOCK = 15
NEW_STOCK_PRICE = 15
STOCK_PURCHASE = 10
STOCK_PURCHASE_PRICE = 11
AUTO_STOCK = 10
AUTO_STOCK_PRICE = 15

def main():
  choice = 0
  stockSum = NEW_STOCK
  billSum = NEW_STOCK_PRICE
  while choice != 'Q':
    getMenu(stockSum, billSum)
    print('\nPlease select B, A, C, or P to continue')
    print('or enter Q to view bill and quit')
    choice = str(input('please make selection')).upper()

    # B--show bill and start a new month
    # --> close month
    # --> display what they owe for that month
    # --> display bars that are lost/unconsumed
    # --> reset availible capacity to 15 bars with a $15 tab
    if choice == 'B':
      print('you choose B')
      print('you owe: $', billSum, '\nYou also donate: ', stockSum,'bars to charity')
      stockSum = NEW_STOCK
      billSum = NEW_STOCK_PRICE

    # A--show availible capacity for current month
    # --> show availible bars but do nothing  print stock
    elif choice == 'A':
      print('you choose A')
      print('you have', stockSum, 'bars left')

    # C--consume bars now
    # --> ask how many bars to consume (1-10)
    # --> subtract from availilbe capacity
    # --> if consume more than capacity--make auto purchase
    # --> calculate with while loop and if/elif/else loop
    elif choice == 'C':
      print('you choose C')
      eat = 'n'
      while eat != 0:
        print('\nSo, how many bars would you like to eat?')
        print('Note: you can only eat 1-10 bars at a time!')
        eat = int(input('Enter number: '))
        if eat == 1 and  stockSum >= 1:
          stockSum =  stockSum - 1
          eat = 0
        elif eat == 1 and  stockSum <= 1:
          stockSum =  stockSum + AUTO_STOCK - 1
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 2 and  stockSum >= 2:
          stockSum =  stockSum - 2
          eat = 0
        elif eat == 2 and  stockSum <= 2:
          stockSum =  stockSum + AUTO_STOCK - 2
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 3 and  stockSum >= 3:
          stockSum =  stockSum - 3
          eat = 0
        elif eat == 3 and  stockSum <= 3:
          stockSum =  stockSum + AUTO_STOCK - 3
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 4 and  stockSum >= 4:
          stockSum =  stockSum - 4
          eat = 0
        elif eat == 4 and  stockSum <= 4:
          stockSum = stockSum + AUTO_STOCK - 4
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 5 and stockSum >= 5:
          stockSum = stockSum - 5
          eat = 0
        elif eat == 5 and stockSum <= 5:
          stockSum = stockSum + AUTO_STOCK - 5
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 6 and stockSum >= 6:
          stockSum = stockSum - 6
          eat = 0
        elif eat <= 6 and sbillSumtockSum <= 6:
          stockSum = stockSum + AUTO_STOCK - 6
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 7 and stockSum >= 7:
          stockSum = stockSum - 7
          eat = 0
        elif eat == 7 and stockSum <= 7:
          stockSum = stockSum + AUTO_STOCK - 7
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 8 and stockSum >= 8:
          stockSum = stockSum - 8
          eat = 0
        elif eat == 8 and stockSum <= 8:
          stockSum = stockSum + AUTO_STOCK - 8
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 9 and stockSum >= 9:
          stockSum = stockSum - 9
          eat = 0
        elif eat == 9 and stockSum <= 9:
          stockSum = stockSum + AUTO_STOCK - 9
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 10 and stockSum >= 10:
          stockSum = stockSum - 10
          eat = 0
        elif eat == stockSum <= 10:
          stockSum = stockSum + AUTO_STOCK - 10
          billSum = billSum + AUTO_STOCK_PRICE
          eat = 0
        elif eat == 0:
          stockSum == stockSum
          print('lost your appetite? :P')
        else:
          print('Error; please enter a whole number between 1-10; or, 0 to quit')

    # P--purchase additional bars
    # --> purchase 1-3 sets of 10 bars
    # --> add to bill and capacity
    # --> calculate with while loop + if/elif/else
    elif choice == 'P':
      print('you choose P')
      buy = 'n'
      while buy != 0:
        print('\nSo, how many sets of bars would you like to buy?')
        print('Note: you can only buy 1-3 sets of 10 bars at a time!\
              \nAlso, 1 set of 10 costs $11')
        buy = int(input('Enter number: '))
        if buy == 1:
          stockSum = stockSum + STOCK_PURCHASE
          billSum = billSum + STOCK_PURCHASE_PRICE
          buy = 0
        elif buy == 2:
          stockSum = stockSum + (STOCK_PURCHASE * 2)
          billSum = billSum + (STOCK_PURCHASE_PRICE * 2)
          buy = 0
        elif buy == 3:
          stockSum = stockSum + (STOCK_PURCHASE * 3)
          billSum = billSum + (STOCK_PURCHASE_PRICE * 3)
          buy = 0
        elif buy == 0:
          billSum = billSum
        else:
          print('Error; please enter a whole number between 1-3; or, 0 to quit')

    # Q--show final bill and quit
    # --> show total bill
    # --> quit loop
    elif choice == 'Q':
      print("you've chosed to quit")
      choice = 'Q'
      print("You have donated all", stockSum, "bars to charity")
      print("You owe: $", billSum, "\nplease pay with BitCoin.")
      stockSum = 0
      billSum = 0
      print("You now have", stockSum, "bars, and now owe, $", billSum)
    else:
      print("Error: invalid selection.")
  print("Thank you!  Have a nice day!")

# function for displaying the menu
# passes the stock and the bill as an argument
def getMenu(x, y):
  print("Availible Bars: ", x)
  print("Cost (so far) this month: $", y)
  print("Menu\tB: Show Bill and start new month")
  print("\tA: Show Availilbe number of bars for current Month")
  print("\tC: Consume bars now")
  print("\tP: Purchase additional bars for current month")
  print("\tQ: show bill and Quit")

# call the main function
main()
