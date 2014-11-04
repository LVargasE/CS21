"""
Assignment 5
CS 21A
Instructor Solution
"""

import random

#define constant global variables
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

# main function
def main():

    playerTotal = 0
    computerTotal = 0
    validGames = 0

    # Play the game 5 times that count, ties do not count.
    while validGames < 5:
        # Get computer number
        computer = random.randint(1,3)
        # Get player number
        player = int(input("Enter 1 for rock, 2 paper, 3 scissors: "))
        while player < 1 or player > 3:
            print("Please choose a value of 1, 2, or 3")
            player = int(input("Enter 1 for rock, 2 paper, 3 scissors: "))
        # end of the while

        print ("You chose", choiceString(player))
        print ("Computer chose", choiceString(computer))
        result = rockPaperScissors(computer, player)

        if result == TIE:
            print("You made the same choice as computer. Starting over\n")
        else:
            validGames += 1

            if result == 1:   #COMPUTER_WINS
                computerTotal += 1
                print ("The computer wins the game\n")
            elif result == 2:  #PLAYER_WINS
                playerTotal += 1
                print ("You win the game\n")

    # end of the while

    print("After 5 runs, the totals are:")
    print("\nYou       ", playerTotal)
    print("\nComputer  ", computerTotal)


# The rockPaperScissors function receives numbers representing the
# computer's and player's choices.
# It returns 0 if there is a tie, 1 the computer won, and 2 if player won.
def rockPaperScissors(computer, player):

    if(computer == player):
        return TIE
    if computer == ROCK :
        if player == PAPER :
            return PLAYER_WINS
        else:  # player == SCISSORS:
            return COMPUTER_WINS


    elif computer == PAPER :
        if player == ROCK :
            return COMPUTER_WINS
        else:  #  player == SCISSORS :
            return PLAYER_WINS


    else: #computer chose scissors
        if player == ROCK :
            return PLAYER_WINS
        else:   #player == PAPER :
            return COMPUTER_WINS


# The choiceString function displays a choice in string format
def choiceString(choice):

    if choice == ROCK :
        return "rock"
    elif choice == PAPER :
        return "paper"
    elif choice == SCISSORS :
        return "scissors"


#Run the main
main()
