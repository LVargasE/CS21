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

class Data:
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
        
        return rowDict
        
class Question(Data):
    """ Question class for preparing data to be used by Game class """
    def __init__(self):
        """ Create list of questions """
        self.question = quesiton
        self.aOne = aOne
        self.aTwo = aTwo
        self.aThree = aThree
        self.aFour = aFour
        self.answer = answer
        self.numAns = numAns
        
    def getQuestions(self):
        # using random to get 10 random numbers between a specific range for 
        # trivia questions
        randomGenerator = random.sample(range(1, 817), 5)
        print(randomGenerator)
        
        # for an individual random number in the sample range --> iterate and use number as
        # index for the trivia questions
        for i in randomGenerator:
            # iterate each element and assign variable
            question = [i][0]
            a1 = ()[i][1]
            a2= self.getData()[i][2]
            a3 = self.getData()[i][3]
            a4 = self.getData()[i][4]
            answer = self.getData()[i][5]
            
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

               
def main():
    triviaData = Data()
    print(triviaData.getData())
    
    questions = Question()
    print(questions.getQuestions())
    
main()