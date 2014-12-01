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

with open('trivia.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    questionIndex = 0
    
    # columns
    questionsColumn = [] 
    Q1Column = []
    Q2Column = []
    Q3Column = []
    Q4Column = []
    answersColumn = []

    
    for row in readCSV:
        question = row[0]
        choiceOne = row[1]
        choiceTwo = row[2]
        choiceThree = row[3]
        choiceFour = row[4]
        answer = row[5]
        
        questionsColumn.append(question)
        Q1Column.append(choiceOne)
        Q2Column.append(choiceTwo)
        Q3Column.append(choiceThree)
        Q4Column.append(choiceFour)
        answersColumn.append(answer)
     
print(questionsColumn)
print(answersColumn)
     
  

        

