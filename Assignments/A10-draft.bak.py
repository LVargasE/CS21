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

class Data:
    def __init__(self):
        ...
    
    def __str__(self):
        ...
        
class Question(Data):
    def __init__(self):
        ...
    def __str__(self)
        
def main():
    # using a dictionary to obtain questions from a trivia question csv file
    triviaData = getData()
    print(len(triviaData))
    
    triviaQuestions = getQuestions(triviaData)
    print(triviaQuestions)
    
    numCorrectAns, numIncorrectAns = getUserResponse(triviaQuestions)
    print('You made', numCorrectAns, 'correct answers and', numIncorrectAns, 'incorrect \
             answers.')

               
# function to open csv file with trivia questions for program   
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
       
main()