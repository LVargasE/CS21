# -*- coding: utf-8 -*-
"""     A10--Trivia Game!
        --> two player trivia game
        --> OOP approach to building the game with classes and objects
"""
import csv
import random

class Question:
    def __init__(self, question, a1, a2, a3, a4, answer, ansNum):
        self.getData = Data('csv')
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.answer = answer
        self.ansNum = ansNum
    
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
        
        aQuestion = Question(question, a1, a2, a3, a4, answer, ansNum)
        return aQuestion
        
    def __getattr__(self, attr):
        return getattr(self.getData, attr)
    
    @classmethod
    def setupAsk(cls, q):
        print('\n', q.question, '\n\t1: ', q.a1, ' \
                 \n\t2: ', q.a2, '\n\t3: ', q.a3, ' \
                 \n\t4: ', q.a4)
        
        while True:
            try:
                choice = int(input("\nWhat's your answer? \n--> "))
            except ValueError:
                print('Sorry, the answer only accepts numbers; please \
                       enter a number 1-4')
            finally:
                if choice in range(1, 5):
                    break
            
        if choice == q.ansNum:
            print('Correct! \n', q.answer)
            return True
        elif choice != q.ansNum:
            print('Incorrect!  \n', q.answer)
            return False   

class Data:
    def __init__(self, filetype):
        self.filetype = filetype
        
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
                    
                    # figure out which answer is correct and assign a variable to it
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

class Game:
    def __init__(self, playerID, gamePoints, totalPoints):
        self.playerID = playerID
        self.gamePoints = gamePoints
        self.totalPoints = totalPoints
    
    def round(self, qClass, data, totalPoints):
        gamePoints = 0
        
        q1 = qClass.getQuestion(data)
        q2 = qClass.getQuestion(data)
        q3 = qClass.getQuestion(data)
        q4 = qClass.getQuestion(data)
        q5 = qClass.getQuestion(data)
        
        if qClass.setupAsk(q1) == True:
            gamePoints = 1
            totalPoints += 1
        if qClass.setupAsk(q2) == True:
            gamePoints += 1
            totalPoints += 1
        if qClass.setupAsk(q3) == True:
            gamePoints += 1
            totalPoints += 1
        if qClass.setupAsk(q4) == True:
            gamePoints += 1
            totalPoints += 1
        if qClass.setupAsk(q5) == True:
            gamePoints += 1
            totalPoints += 1
            
        print('you won {} points this game and have {} total \
               points from previous games.'.format(gamePoints, totalPoints))
        
        return totalPoints
        
def main():
    totalPointsP1 = 0
    totalPointsP2 = 0
    
    data = Data('csv')
    questionsData = data.getData()
    
    questions = Question('question', 'a1', 'a2', 'a3', 'a4', \
                         'answer', 'ansNum')
                         
    print('\nROUND ONE//\nPlayer One')
    playerOne = Game(str(input('Enter your name: ')), 0, 0)
    p1round1 = playerOne.round(questions, questionsData, totalPointsP1)
    
    print('\nSwitch Players\n')
    
    print('\nROUND ONE//\nPlayer Two')
    playerTwo = Game(str(input('Enter your name: ')), 0, 0)
    p2round1 = playerTwo.round(questions, questionsData, totalPointsP2)
    
    if p1round1 < p2round1:
        print('{} is the winner with {} total \
              points!'.format(playerTwo.playerID, p2round1))
    elif p2round1 < p1round1:
        print('{} is the winner with {} total \
              points!'.format(playerOne.playerID, p1round1))
    
main()
