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

def lookUpRecords(name, score, searchName):

    loadRecords(name, score)

    search = records.get(searchName, 0)

    if search != 0:
        print('Name found in Records.')
        return True
    else:
        print('Name not found in Records.')
        return False

    return searchName


def addRecords(name, score, searchName):

    infile = open("Golfers.txt", "a")

    name = searchName
    score = int(input("Enter the golfer's score:\n--> "))

    # append to the file
    print('Writing to file...\n...\n...\n...')
    infile.write(name + '\n')
    infile.write(str(score) + '\n')
    print('File successfully written.')

def removeRecords():
    pass


def saveRecords():
    pass


def getMenu():

    print('Please make a selection from the Menu below:\
          \n\t(C) make a Change to one of the records\
          \n\t(A) Add a record to the file\
          \n\t(R) Remove a record from the file\
          \n\t(D) Display the file with all records\
          \n\t(Q) Quit the program')


def main():

    # local variables
    choice = ''
    found = False
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
    print("\nYou are going to add a record")

    searchName = input('\nPlease enter the name of the golfer \
                        \nyou would like to add to the record. \
                        \n\ne.g., Tiger Woods (given name, surname). \
                        \n\n--> ')

    lookUpRecords(name, score, searchName)
    print(type(found))
    print(found)

    found = lookUpRecords(name, score, searchName)

    if found == True:
        print('Name already exists in Records; cannot write to file.')
    else:
        addRecords(name, score, searchName)

        lookUpRecords(name, score, searchName)

        found = lookUpRecords(name, score, searchName)
        print(searchName)
        print(type(found))
        print(found)
        if found != True:
            print('Record unsuccessfully added to file.')
        else:
            print('Record was successfully added to file.')

main()
