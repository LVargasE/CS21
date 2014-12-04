# -*- coding: utf-8 -*-
"""     A10--Trivia Game!
        --> two player trivia game
        --> OOP approach to building the game with classes and objects
"""
import csv
import random

class Question:
    pass

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
            
                # reading the trivia questions
                for row in readCSV:
                    rowDict[index] = row
                    print(type(row))
                    print(type(rowDict))
                    """
                    question = rowDict[0]
                    a1 = rowDict[1]
                    a2 = rowDict[2]
                    a3 = rowDict[3]
                    a4 = rowDict[4]
                    answer = rowDict[5]
                    
                    # figure out which answer is correct and assign a variable to it
                    if answer == a1:
                        ansNum = rowDict.append(1)
                    elif answer == a2:
                        ansNum = rowDict.append(2)
                    elif answer == a3:
                        ansNum = rowDict.append(3)
                    elif answer == a4:
                        ansNum = rowDict.append(4)
                    else:
                        print("Error!  No correct answer")
                    # place questions into new dictionary in the right order
                    rowDict[index] = [question, a1, a2, a3, a4, \
                                            answer, ansNum]
                    """
                    return rowDict
                    
        except IOError:
            print("The file could not be found.")
            

class Game:
    def __init__(self, gamePoints, totalPoints):
        self.gamePoints = gamePoints
        self.totalPoints = totalPoints

def main():
    data = Data('csv')
    questionsData = data.getData()
    print(questionsData)

main()
