# -*- coding: utf-8 -*-
"""   A10--Trivia Game! 
      --> two player trivia game
      --> OOP approach to building the game with classes and objects
"""
import csv
import random
               
# the Data class enables the main function to pass the data from a CSV file 
# through methods that place the data in a dictionary with numbers as keys 
# and a list as the value
class Data():
    # the init method has one attribupte and other methods that andable the
    # main funciton to affect the object to do the data janitorial work 
    # necessary for processing in the game
    def __init__(self, triviaData):
        self.triviaData = triviaData
    
    # uses the CSV dictionary and separates questions into keys (numbers for
    # questions) and values (a list that contains all the Question class
    # attributes that aren't parsed)
    def getQuestions(self, triviaData):
        # local variables
        index = 0
        questionsDict =  {}
        
        # iterates through all the data to organize into a nested list
        for i in range(1, 816):
            question = triviaData[i][0]
            a1 = triviaData[i][1]
            a2= triviaData[i][2]
            a3 = triviaData[i][3]
            a4 = triviaData[i][4]
            answer = triviaData[i][5]
            
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
            questionsDict[index] = [question, a1, a2, a3, a4, answer, ansNum]
            index += 1

        return questionsDict
        
# the Game class class allows for easy parsing of question attributes from
# nested lists for easier handling and processing         
class Game(Data):
    def __init__(self, triviaData, question, a1, a2, a3, a4, answer, ansNum, \
                 ansCorrect, ansIncorrect, roundWins):
        Data.__init__(self, triviaData)
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.answer = answer
        self.ansNum = ansNum
        self.ansCorrect = ansCorrect
        self.ansIncorrect = ansIncorrect
        self.roundWins = roundWins                                                       

    # method for parsing a single question and create an instance from the 
    # Question class to return to main
    def parseQuestions(self, aDict, qNum):
        for i in aDict[qNum]:
            question = aDict[qNum][0]
            a1 = aDict[qNum][1] 
            a2 =aDict[qNum][2]
            a3 = aDict[qNum][3]
            a4 = aDict[qNum][4]
            answer = aDict[qNum][5]
            ansNum = aDict[qNum][6] 
            
            # instantiates the object
            aTriviaQuestion = Game(question, a1, a2, a3, a4, answer, ansNum)

        return aTriviaQuestion
    
    def setUpQuestions(self, triviaData, question, a1, a2, a3, a4, answer, ansNum, \
                 ansCorrect, ansIncorrect, roundWins):

        # call the method from Data class to get all the questions
        triviaData = data.getQuestions(data.triviaData)
        
        # use the random module's sample method to select five random numbers
        randomGen = random.sample(range(1, 817), 5)
        
        # instantiates by calling the Data class method parseQuestions 
        qOne = data.parseQuestions(triviaData, randomGen[0])
        qTwo = data.parseQuestions(triviaData, randomGen[1])
        qThree = data.parseQuestions(triviaData, randomGen[2])
        qFour = data.parseQuestions(triviaData, randomGen[3])
        qFive = data.parseQuestions(triviaData, randomGen[4])
        
        # set up an instance of Game for player one
        playerOne = Game(qOne.triviaData, question, qOne.a1, qOne.a2, qOne.a3,\
                         qOne.a4, qOne.answer, qOne.ansNum, 0, 0, 0)
        
        p1aCorr, p1aInCorr = playerOne.askQuestions(qOne.question, qOne.a1,\
                                                    qOne.a2, qOne.a3, qOne.a4,\
                                                    qOne.answer, qOne.ansNum,\
                                                    0, 0, 0)
    
    def askQuestions(self, question, a1, a2, a3, a4, answer, ansNum, \
                     ansCorrect, ansIncorrect, roundWins):

        print('THE SCORE SO FAR//\n\n\t Rounds Won: ', roundWins, '\n')
        
        print('\nFIRST QUESTION//\n', question, '\n\t1: ', a1, ' \
                 \n\t2: ', a2, '\n\t3: ', a3, ' \
                 \n\t4: ', a4)
           
        while True:
            try:
                choice = int(input("\nWhat's your answer? \n--> "))
            except ValueError:
                print('Sorry, the answer only accepts numbers; please \
                       enter a number 1-4')
            finally:
                if choice in range(1, 5):
                    break
           
            if choice == ansNum:
                ansCorrect += 1
            elif choice != ansNum:
                ansIncorrect += 1
            
        return ansCorrect, ansIncorrect

# main function        
def main():
    # instantiate the Data class and assign the variable 'data'
    data = Data(getData())
    
    print('NOW SWITCH PLAYERS')
    
    # set up an instance of Game for player two
    playerTwo = Game(qOne.question, qOne.a1, qOne.a2, qOne.a3, \
                     qOne.a4, qOne.answer, qOne.ansNum, 0, 0, 0)
    
    p2aCorr, p2aInCorr = playerOne.askQuestions(qOne.question, qOne.a1, \
                                                qOne.a2, qOne.a3, qOne.a4,  \
                                                qOne.answer, qOne.ansNum, \
                                                0, 0, 0)
            
    
# function outside of class to open the file and close the file where the 
# trivia questions are housed.      
def getData():
        # make sure there isn't an IO error
        try:
            # open the csv file + use an index accumulator for dictionary
            with open('trivia.csv') as csvFile:
                readCSV = csv.reader(csvFile, delimiter=',')
                index = 0
                
                # questions, answer choices, and answers dictionary
                rowDict = {}
            
                # reading the trivia questions
                for row in readCSV:
                    rowDict[index] = row
                    index += 1
    
        except IOError:
            print("The file could not be found.")
        
        return rowDict
        
main()