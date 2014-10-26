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

import random

# main program
def main():
  # local variables
  pythonWins = 0
  youWin = 0
  youDraw = 0
  choice = 0

  getIntro()

  while choice != 'Q':
    choice = int(input('Your move. \
                    \nOr, do you give up?\
                    \n\nEnter Q to quit and review scores.\n\n-->'))
    if choice == 1 or 2 or 3:
      # ...
      print("One\nTwo\nThree")

      pythonChoice = random.randrange(1,4)

      choiceStr = num2str(choice)
      pythonChoiceStr = num2str(pythonChoice)

      whoWins = (choice - pythonChoice) % 3

      if whoWins == 1:
        winner = 'You'
        youWin += 1
      elif whoWins == 2:
        winner = 'Python'
        pythonWins += 1
      elif whoWins == 0:
        winner = 'Nobody'
        youDraw += 1

      getWinner(choiceStr, pythonChoiceStr, winner)

    elif choice == 'H' or choice == 'h':
      getIntro()
    elif choice == 'Q' or choice == 'q':
      print('You win: ', youWin, 'times!\
            \nPython wins: ', pythonWins, 'times!')
      if youWin <= pythonWins:
        print("\nThere's no clear winner here; what a draw.")
      elif youWin < pythonWins:
        print("Python bested you this time...\
              \nBetter luck next time!")
      elif youWin > pythonWins:
        print("you really stuck it to the man! You're the victor!")
    else:
      print('Please enter either:\
            \t1 for Rock\n\t2 for Paper\n\t3 for Scissors\
            \n\n"help" for intro rules.\n"Q" to Quit.')

def getIntro():
  print('Python wants to play a game with you!\
         \nHow about Rock, Paper, Scissors?')
  print('Ok. Remember these values and what they are associated with:\
        \n\t (1) means Rock\
        \n\t (2) means Paper\
        \n\t (3) means Scissors')
  print('\nHere are the rules of the game:\
        \n\t Paper covers Rock\
        \n\t Rock smashes Scissors\
        \n\t Scissors cut Paper\
        \n\n\t Paper/Paper, Rock/Rock, or Scissors/Scissors means a tie.')
  print('\n\n Are you ready?')

def num2str(num):
  if num == 1:
    return 'Rock'
  elif num == 2:
    return 'Paper'
  elif num == 3:
    return 'Scissors'

def getWinner(choiceStr, pythonChoiceStr, winner):
  print("You've chosen", choiceStr,"\
        \nPython has chosen", pythonChoiceStr)
  if winner == 'You':
    print('You win!')
  elif winner == 'Python':
    print('Sorry.  Python wins.')
  elif winner == 'Nobody':
    print("Well, it's a draw")
  return choiceStr, pythonChoiceStr, winner


# call the main function
main()
