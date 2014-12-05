# -*- coding: utf-8 -*-
"""     A10--Trivia Game!
        --> two player trivia game
        --> OOP approach to building the game with classes and objects
"""
import csv
import random

# the Question class acts as a placeholder for the parts of the question
# needed to construct questions and check answers
class Question:
    # __init__ uses the Data class method getData through composition
    def __init__(self, question, a1, a2, a3, a4, answer, ansNum):
        self.getData = Data('csv')
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.answer = answer
        self.ansNum = ansNum

    # the method performs better as a class method since it instantiates the
    # Question class with sample questions for the game
    @classmethod
    def getQuestion(cls, triviaDict):
        # using random to get 10 random numbers between a specific range for
        # trivia questions
        randomGenerator = random.sample(range(1, 817), 1)

        # for an individual random number in the sample range
        # --> iterate and use number as index for the trivia questions
        for i in randomGenerator:
            question = triviaDict[i][0]
            a1 = triviaDict[i][1]
            a2= triviaDict[i][2]
            a3 = triviaDict[i][3]
            a4 = triviaDict[i][4]
            answer = triviaDict[i][5]
            ansNum = triviaDict[i][6]

        # this creates an instance to return (from question class)
        aQuestion = Question(question, a1, a2, a3, a4, answer, ansNum)
        return aQuestion

    # this is a part of using composition rather than inheritance to get the
    # attributes from the getData method
    def __getattr__(self, attr):
        return getattr(self.getData, attr)

    # this method sets up the question (also checks answer)
    @classmethod
    def setupAsk(cls, q):
        print('\n', q.question, '\n\t1: ', q.a1, ' \
                 \n\t2: ', q.a2, '\n\t3: ', q.a3, ' \
                 \n\t4: ', q.a4, '\n')

        # make sure the user's input works
        while True:
            try:
                choice = int(input("\nWhat's your answer? \n--> "))
            except ValueError:
                print('\nSorry, the answer only accepts numbers; please \
                       enter a number 1-4')
                choice = int(input("\nWhat's your answer? \n--> "))
            finally:
                if choice in range(1, 5):
                    break

        # if the question is correct, return true; if not, return false
        if choice == q.ansNum:
            print('\nCorrect! \n', q.answer)
            return True
        elif choice != q.ansNum:
            print('\nIncorrect!  \n', q.answer)
            return False

# the Data class handles openning the file and preparing it to be used by
# the Question and Game class
class Data:
    def __init__(self, filetype):
        self.filetype = filetype

    # opens the CSV to read and prepare it to be used in computaiton later
    @classmethod
    def getData(cls):
        # make sure there isn't an IO error
        try:
            # open the csv file + use an index accumulator for dictionary
            with open('trivia.csv') as csvFile:
                readCSV = csv.reader(csvFile, delimiter=',')
                index = 0

                # questions, answer choices, and answers dictionary
                rowDict = {}
                questionData = {}
                # reading the trivia questions
                for row in readCSV:
                    rowDict[index] = row
                    question = rowDict[index][0]
                    a1 = rowDict[index][1]
                    a2 = rowDict[index][2]
                    a3 = rowDict[index][3]
                    a4 = rowDict[index][4]
                    answer = rowDict[index][5]

                    # figure out which answer is correct and assign a variable
                    if answer == a1:
                        ansNum = 1
                    elif answer == a2:
                        ansNum = 2
                    elif answer == a3:
                        ansNum = 3
                    elif answer == a4:
                        ansNum = 4
                    else:
                        print("Error!  No correct answer")

                    # place questions into new dictionary in the right order
                    questionData[index] = [question, a1, a2, a3, a4, \
                                            answer, ansNum]
                    index += 1

                return questionData

        except IOError:
            print("The file could not be found.")

# the Game class is where the bulk of the game's structure is found
class Game:
    def __init__(self, playerID, gamePoints):
        self.playerID = playerID
        self.gamePoints = gamePoints

    # method to create instances for questions and find out if a quesiton
    # was answered correctly or not
    def round(self, qClass, data):
        gamePoints = 0 # reset to 0 for new round

        # instances
        q1 = qClass.getQuestion(data)
        q2 = qClass.getQuestion(data)
        q3 = qClass.getQuestion(data)
        q4 = qClass.getQuestion(data)
        q5 = qClass.getQuestion(data)

        # return value is true or false; this computes points
        if qClass.setupAsk(q1) == True:
            gamePoints += 1
        if qClass.setupAsk(q2) == True:
            gamePoints += 1
        if qClass.setupAsk(q3) == True:
            gamePoints += 1
        if qClass.setupAsk(q4) == True:
            gamePoints += 1
        if qClass.setupAsk(q5) == True:
            gamePoints += 1

        # let the user know what happenned this round
        print('you won {} points this game!'.format(gamePoints))

        return gamePoints

def main():
    # local variables
    flag = False
    gameNum = 1

    # instance of Data class
    data = Data('csv')
    questionsData = data.getData()

    # instance of Question class with filler data
    questions = Question('question', 'a1', 'a2', 'a3', 'a4', \
                         'answer', 'ansNum')

    # create both players
    playerOne = Game(str(input('PLAYER ONE//\nEnter your name: ')), 0,)
    playerTwo = Game(str(input('PLAYER TWO//\nEnter your name: ')), 0,)

    # while loop to keep the game going if the user chooses
    while flag != True:
        # let the user know which round they're playing
        print('\nROUND ', gameNum, '//\nPlayer One')

        # first player instance; asks five questions
        p1round = playerOne.round(questions, questionsData)

        print("""
        +++++++++++++++++++++++++++++++++++++++++++++++++
        +                   SWITCH PLAYERS!             +
        +++++++++++++++++++++++++++++++++++++++++++++++++
        """)

        # let the user know to switch players
        print('\nROUND ', gameNum, '//\nPlayer Two')

        # second player instance; asks the five quesitons
        p2round = playerTwo.round(questions, questionsData)
        
        # let the user know which round they are on with accumulator
        gameNum += 1

        # figure out who won and use user's inputed name and their points
        # in print statement
        if p1round < p2round:
            print('Thank you for playing!  {} is the winner with {} total \
                  game points!'.format(playerTwo.playerID, p2round))
        elif p2round < p1round:
            print('Thank you for playing!  {} is the winner with {} total \
                  game points!'.format(playerOne.playerID, p1round))
        elif p2round == p1round:
            print('There was a tie!  Both {} and {} both earned {} total \
                   game points; but you are both still \
                   winners!'.format(playerOne.playerID, playerTwo.playerID, \
                   p1round))
        
        # find out if user wants to continue + validate user response
        while True:
            try:
                choice = str(input("\nKeep playing? \n--> ")).upper()
            except ValueError:
                print("Sorry, enter either a 'Y' for 'Yes', or 'N' for 'No'.")
            finally:
                if choice == 'N':
                    flag = True
                    break
                if choice == 'Y':
                    break
                else:
                    print("please enter either a 'Y' for 'Yes', or 'N' \
                           for 'No'.")
    
    # say bye to players and quit the program
    print('\nThank you for playing!  See you next time!\n')

main()
