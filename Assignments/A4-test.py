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

choice = ''

print('Please select B, A, C, or P to continue')
print('or enter Q to view bill and quit')
programOptions = input('Your choice: ')
