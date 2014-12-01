# -*- coding: utf-8 -*-
"""
A10--Trivia Game! // Trivia games are very popular with questions for 
each player.  We are going to make a 2 player game with the questions 
and answers being stored in a class. 

The Program Spec:

--> Each question will have 4 possible answers.  
--> Each player will take turns with the questions.  
--> There will be a total of 10 questions, each player getting a chance  
    to answer 5 of them.  If the player selects the correct answer,  
    they earn a point. Tell the player whether they got it right or 
    wrong.
 
After answers have been selected for all the questions, the program 
displays the number of points earned by each player and declares the 
player with the highest number of points the winner. If there is a tie, 
announce that.
 
--> Create a Question class to hold the data for a trivia question.  
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
 
Create a value-returning function named createQuestionsAnswers( ) that 
creates a list containing 10 question objects, one for each trivia 
question.  Make up your own trivia questions and answers on the 
subjects of your choice and hard code them in this function.
 
The main() should call createQuestionsAnswers( ) and then use that 
returned list to display the question for each player in turn.  
Validate the user's choice to keep it between 1 and 4.  Keep track of 
the number of correct answers and display the winner, or tie, at the 
end.  
 
Be sure to include comments in your code.
 
Create a run and include it as output with your program.  
Be sure to show that the validation works for the possible answers.

"""
import csv
import random

def main():
    # using a dictionary to obtain questions from a trivia question csv file
    triviaQuestions = getQuestions()
    print(len(triviaQuestions))
    
    # using random to get 10 random numbers between a specific range for 
    # trivia questions
    randomGenerator = random.sample(range(1, 817), 10)
    print(randomGenerator)
    
    for i in randomGenerator:
        print(triviaQuestions[i][0])
        print("What's your answer?\n--> ")
    
    
# function to open csv file with trivia questions for program   
def getQuestions():
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