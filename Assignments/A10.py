"""
A10--Trivia Game!

Create a Question class to hold the data for a trivia question.  
  The class should have the attributes for the following data:
    A trivia question
    Possible answer 1
    Possible answer 2
    Possible answer 3
    Possible answer 4
    The number of the correct answer (1, 2, 3, or 4)
 
The Question class should also have an appropriate __init__ method, 
accessors, mutators, and a __str__ method.  Add other methods if you 
wish.

"""
import csv
import random

class Data:
    """ ... """
    def __init__(self):
        """ ... """
        self.triviaData = 
    
    # function to open csv file with trivia questions for program   
    def getData(self):
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
        
        return self.questionsDict
        
class Question(Data):
    """ Question class for preparing data to be used by Game class """
    def __init__(self):
        """ Create list of questions """
        self.triviaQuestion = initQ
        self.answerOne = initA1
        self.answerTwo = initA2
        self.answerThree = initA3
        self.answerFour = initA4
        self.answer = initA
        self.intAnswer = initIntA
    
    
    # ...
    def getQuestions(triviaDict):
        index = 0    
        questionsDict =  {}
        
        # using random to get 10 random numbers between a specific range for 
        # trivia questions
        randomGenerator = random.sample(range(1, 817), 10)
        print(randomGenerator)
        
        # for an individual random number in the sample range --> iterate and use number as
        # index for the trivia questions
        for i in randomGenerator:
            # iterate each element and assign variable
            question = triviaDict[i][0]
            a1 = triviaDict[i][1]
            a2= triviaDict[i][2]
            a3 = triviaDict[i][3]
            a4 = triviaDict[i][4]
            answer = triviaDict[i][5]
            
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
    
    # ...
    def getUserResponse(triviaDict):   
        correctAns = 0
        incorrectAns = 0
        
        for i in triviaDict:
            print('\n', triviaDict[i][0], '\n\t1: ', triviaDict[i][1], ' \
                     \n\t2: ', triviaDict[i][2], '\n\t3: ', triviaDict[i][3], ' \
                     \n\t4: ', triviaDict[i][4])
           
            while True:
                try:
                    choice = int(input("\nWhat's your answer? \n--> "))
                except ValueError:
                    print('Sorry, the answer only accepts numbers; please enter a number 1-4')
                finally:
                    if choice in range(1, 5):
                        break
           
            if choice == triviaDict[i][6]:
                correctAns += 1
            elif choice != triviaDict[i][6]:
                incorrectAns += 1
            
        return correctAns, incorrectAns
        
    def __str__(self):
        return ...
        
class Game:
    """ Game class for setting up the structure of the game """
    def __init__(self):
         """ ... """
         ...