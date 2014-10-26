"""
A5 --> Rock, Paper, Scissors

 use random number (1-3)
 don't show the computer's number!
 have user enter their choice
 display the computer's choice as a word; not a number
 winner selected
 winner congratulated

 program specs
 --> main() calls functions and passes arguments
 --> create value returning function named rockPaperScissors(computer, player)
     that receives numbers for the user/player and computer
 --> value returning function named choiceString(choice)
"""
# import the random number module
import random

# main program
def main():
  # local variables to calculate total wins to display at end
  pythonWins = 0
  youWin = 0
  youDraw = 0
  choice = 0

  # intro with rules and all options
  getIntro()

  # while loop to decide to display game, help, + exit functions
  while choice != 5:
    choice = int(input('Your move.\
                    \nOr, do you give up?\
                    \n\nEnter 4 for the intro rules/help +\
                    \nEnter 5 to quit and review scores.\n\n-->'))

    if choice == 1 or choice == 2 or choice == 3:
      # simulate the fists going up and down once, twice, thrice
      print("\tOne\n\tTwo\n\tThree")

      # use function from random module to pass random int numbers
      pythonChoice = random.randrange(1,4)

      # the next two functions convert the number into their str equivalents
      choiceStr = num2str(choice)
      pythonChoiceStr = num2str(pythonChoice)

      # algorithm for determining winner
      # in all 9 of the possible choices, the user's choice subtracted by
      # the computer's choice mod/remainder 3 (for the amount of numbers)
      # will result in either a 1 (for the user), or 2 (for the computer)
      # this tells us who won (1/user, or 2/computer)
      whoWins = (choice - pythonChoice) % 3

      # whoever wins has their local variable increased by one to keep track
      if whoWins == 1:
        winner = 'You'
        youWin += 1
      elif whoWins == 2:
        winner = 'Python'
        pythonWins += 1
      elif whoWins == 0:
        winner = 'Nobody'
        youDraw += 1

      # function to determin winner and print results
      getWinner(choiceStr, pythonChoiceStr, winner)

    # remaining choices that are non-game related
    elif choice == 4:
      getIntro()
    elif choice == 5:
      print('You win: ', youWin, 'times!\
            \nPython wins: ', pythonWins, 'times!')
      # quick if/elif loop to print the right phrasing for the winner
      if youWin == pythonWins:
        print("\nThere's no clear winner here; what a draw.")
      elif youWin < pythonWins:
        print("Python bested you this time...\
              \nBetter luck next time!")
      elif youWin > pythonWins:
        print("you really stuck it to the man! You're the victor!")
    # just to ensure no other ints are entered (only 1-5)
    else:
      print('Please enter either:\
            \n\t1 for Rock\n\t2 for Paper\n\t3 for Scissors\
            \n\n"4" for intro rules.\n"5" to Quit.')

# this is the intro to the game with rules and values
def getIntro():
  print('Python wants to play a game with you!\
         \nHow about Rock, Paper, Scissors?')
  print('Ok. Remember these values and what they are associated with:\
        \n\t(1) means Rock\
        \n\t(2) means Paper\
        \n\t(3) means Scissors')
  print('\nHere are the rules of the game:\
        \n\tPaper covers Rock\
        \n\tRock smashes Scissors\
        \n\tScissors cut Paper\
        \n\n\tPaper/Paper, Rock/Rock, or Scissors/Scissors means a tie.')
  print('\n\nAre you ready?')

#function that converts the number to the str equivalent
def num2str(num):
  if num == 1:
    return 'Rock'
  elif num == 2:
    return 'Paper'
  elif num == 3:
    return 'Scissors'

# function to determin and print the winner!
def getWinner(choiceStr, pythonChoiceStr, winner):
  print("\tYou've chosen", choiceStr,"\
        \n\tPython has chosen", pythonChoiceStr,'\n')
  if winner == 'You':
    print('\n\tYou win!\n')
  elif winner == 'Python':
    print('\n\tSorry.  Python wins.\n')
  elif winner == 'Nobody':
    print("\n\tWell, it's a draw\n")
  return choiceStr, pythonChoiceStr, winner

# call the main function
main()
