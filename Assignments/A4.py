# Assignment 4
# The candy locker

# Each month all candybar stock returns to 0
# --> then, new stock is added (15 bars for $15)
# --> bars can only be consumed 1-10 bars at a time
# ----> which is to say, it takes two sessions to consume 15 bars

# Named constant
NEW_STOCK = 15
NEW_STOCK_PRICE = 15

# Two ways to consume--a less expensive way and a more expensive way
# Way 1--PLANED: buy before reaching 0 availible bars
# --> purchase 10 bars for $11
# ----> can only purchase 30 bars at once ($33), but can make infinite purcases a month

# Named constant
STOCK_PURCHASE = 10
STOCK_PURCHASE_PRICE = 11

# Way 2--AUTOMATIC: consume negative bars that are purchased automatically
# --> automatic 10 bars for $15 (10 bars garuntees enough for one session)

# Named constant
AUTO_STOCK = 10
AUTO_STOCK_PRICE = 15

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

def getUserInput():
  # ?? not sure if this will work
  theBill = bill()
  whatsAvailible = availible()
  toConsume = consume()
  toPurchase = purchase()
  pleaseQuit = quit()

  # other option
  options = []
  programOptions = "'B', 'A', 'C', 'P'"
  print('Please select B, A, C, or P to continue')
  print('or enter Q to view bill and quit')
  programOptions = input('Your choice: ').upper()
  # example from other student is to do choice = (input('please make selection')).upper()

  # Continue program unless user selects Q
  while x != 'Q':

def choice loop(x, y, z, p, q):
  if x = 'B':
    y = bill()
  elif x = 'A':
    z = availible()
  elif x = 'C'
    p = consume()
  elif x = 'P'
    q = purchase()
  else




# need 5 separate funcitons:

# B--show bill and start a new month
# --> close month
# --> display what they owe for that month
# --> display bars that are lost/unconsumed
# --> reset availible capacity to 15 bars with a $15 tab
def bill():
  bill = 0
  bars = 0
  while

# A--show availible capacity for current month
# --> show availible bars but do nothing
def availible():

# C--consume bars now
# --> ask how many bars to consume (1-10)
# --> subtract from availilbe capacity
# --> if consume more than capacity--make auto purchase
def consume():

# P--purchase additional bars
# --> purchase 1-3 sets of 10 bars
# --> add to bill and capacity
def purchase():

# Q--show final bill and quit
# --> show total bill (don't show capacity)
# --> quit loop
def quit():

# validate user entered variables and allow for 'b' or 'B'

# one run
def main():
  while keepGoing != 'Q' or 'q':
    getMenu()

main()
