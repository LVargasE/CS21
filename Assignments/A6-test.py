"""
names of things:
 choice = ''
 found = ''
 getMenu()
 changeRecord(searchName, score)
 addRecord(name, score)
 removeRecord(searchName)
 disploayRecords()

"""

import os

choice = ''
found = ''
records = {}

def loadRecords(k, y):
  # open the original Golfers.txt file to print all records
  infile = open("Golfers.txt", "r")

  # read the first record's 'name' field
  k = infile.readline()

  # read rest of file
  while k != '':
      # read the score field
      v = infile.readline()

      # strip the '\n' from 'name'
      k = k.rstrip('\n')
      v = v.rstrip('\n')

      # send name and score to dictionary
      records["k"] = v

      # read next name
      k = infile.readline()

    # close file
    infile.close()

def displayRecords():
  print('Golfers Records:\n')

  # call function to load records
  loadRecords(name, score)

  # print all records
  for (name, score) in records.items():
    print("Golfer's Name: ", name, "\tGolfer's Score: ", score)

def addRecords(var):

def lookUpRecords(var):

def removeRecords(var):

def saveRecords(var):

def getMenu():

def main():
  loadRecords(name, score)
  displayRecords()

main()
