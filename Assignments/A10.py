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
# -*- coding: utf-8 -*-
"""
A10--Trivia Game! // Trivia games are very popular with questions for 
each player.  We are going to make a 2 player game with the questions 
and answers being stored in a class. 

The Program Spec:
 
--> Create a Question class to hold the data for a trivia question.  
    The class should have the attributes for the following data:
        A trivia question
        Possible answer 1
        Possible answer 2
        Possible answer 3
        Possible answer 4
        The number of the correct answer (1, 2, 3, or 4)

"""
import csv
import random

class Question():
    def __init__(self, question, a1, a2, a3, a4, answer, ansNum):
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.answer = answer
        self.ansNum = ansNum
               
# the Data class opens the CSV file, reads the rows and converts rows to trivia questions
# in a dictionary with numbers as keys and a list as the value
class Data():
    def __init__(self, triviaData):
        self.triviaData = triviaData
    
    def getQuestions(self, triviaData):
        index = 0
        questionsDict =  {}
        
        for i in range(1, 816):
            question = triviaData[i][0]
            a1 = triviaData[i][1]
            a2= triviaData[i][2]
            a3 = triviaData[i][3]
            a4 = triviaData[i][4]
            answer = triviaData[i][5]
            
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
        
    def parseQuestions(self, aDict, qNum):
        for k in aDict[qNum]:
            print(k)
            question = aDict[qNum][0]
            a1 = aDict[qNum][1] 
            a2 =aDict[qNum][2]
            a3 = aDict[qNum][3]
            a4 = aDict[qNum][4]
            answer = aDict[qNum][5]
            ansNum = aDict[qNum][6] 

            aTriviaQuestion = Question(question, a1, a2, a3, a4, answer, ansNum)

        return aTriviaQuestion
        
def main():
    data = Data(getData())
    print(data)
    triviaData = data.getQuestions(data.triviaData)
    randomGen = random.sample(range(1, 817), 5)
    print(randomGen[0])
    
    qOne = data.parseQuestions(triviaData, randomGen[0])
    qTwo = data.parseQuestions(triviaData, randomGen[1])
    qThree = data.parseQuestions(triviaData, randomGen[2])
    qFour = data.parseQuestions(triviaData, randomGen[3])
    qFive = data.parseQuestions(triviaData, randomGen[4])
    
    print(qOne.question, '\n', qOne.a1, '\n', qOne.a2, '\n', qOne.a3, '\n', qOne.a4, '\n', qOne.answer, ' \
             \n', qOne.ansNum)
    
    print(qTwo.question, '\n', qTwo.a1, '\n', qTwo.a2, qTwo.a3, '\n', qTwo.a4, '\n', qTwo.answer, ' \
             \n', qTwo.ansNum)
    
    """
    questionOne = data.parseQuestions(data.triviaData, 1)
    print(questionOne.question)
    questionTwo = data.parseQuestions(data.triviaData, 2)
    print(questionTwo.question)
    """

    
    
    
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
def randomGenerator():
    # using random to get 10 random numbers between a specific range for 
        # trivia questions
        randomGenerator = random.sample(range(1, 817), 5)
        print(randomGenerator)
        """
        # for an individual random number in the sample range --> iterate and use number as
        # index for the trivia questions
        for i in randomGenerator:
            # iterate each element and assign variable      
        """
main()