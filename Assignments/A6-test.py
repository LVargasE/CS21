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

records = {}

def loadRecords(k, v):
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
      records[k] = v

      # read next name
      k = infile.readline()

  # close file
  infile.close()

def displayRecords(name, score):
  print('Golfers Records:\n')

  # call function to load records
  loadRecords(name, score)

  # print all records
  for (name, score) in records.items():
    print("Golfer's Name: ", name, "\t\tGolfer's Score: ", score)

def lookUpRecords(found, name, score, searchName):
  found = False

  while found != True:
      loadRecords(name, score)

      if searchName in records:
          print('Name found')
          found = True
      else:
          searchName = input("\nGolfer not found in file.\
                              \nEnter golfer's full name,\
                              \ne.g., Tiger Woods, below:\
                              \n\t--> ")
      return found, searchName

def addRecords(found, name, score, searchName):
  # use bool var as flag
  found = False

  while found != False:
      # next --> need to load file to set up search
      loadRecords(name, score)

      # then --> search user input to make sure we're not adding duplicate records
      if searchName in records:
          print("Error; name already exists in records.")
          found = True
          return found
      else:
          infile = open("Golfers.txt", "a")

          name = searchName
          score = int(input("Enter the golfer's score:\t--> "))

          # append to the file
          infile.write(name + '\n')
          infile.write(str(score) + '\n')
          found = False
          return found

def removeRecords(var):
  pass

def saveRecords(var):
  pass

def getMenu():
  pass

def main():
  # local variables
  choice = ''
  found = ''
  name = ''
  score = ''

  # load records
  loadRecords(name, score)

  # display records
  displayRecords(name, score)

  # search records
  # searchName = input('enter name: ')
  # lookUpRecords(found, name, score, searchName)

  # add to record
  print("you are going to add a record")

  searchName = input('Please enter the name of the golfer \
                      you would like to add to the record. \
                      \n\ne.g., Tiger Woods (given name, surname) \
                      \n\n--> ')

  addRecords(found, name, score, searchName)

  while found == False:
    print('Record sucessfully added to file')
    found = True
  else:
    print("didn't work")




main()
