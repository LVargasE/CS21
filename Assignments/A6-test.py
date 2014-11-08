"""
A5 --> Golf Scores

 program specs:
 -->  Display all records in the file, then enter user-input
      loop with a 5 value menu at each pass of the loop (use a function)
 -->  User enters single letter only (use validation)
 -->  The user can change one of the records (C), add a record to the file (A),
      remove a record from the file (R), display all the records (D), or
      quit (Q).
 program tips:
 -->  Always validate user input
 -->  Don't need to test for non-numeric values when user asked to enter numbers
 -->  Submit a run that shows everything with several passes of the loop
      all choices must be used twice in random order (except Q)--show one
      illegal choice/bad choice

"""
# needed to remove/rename files
import os

# blank dictionary to send info from files to for easier handling/searching
records = {}

# main function to process menu options and interpret return values
def main():
    # local variables
    choice = ''
    found = False
    name = ''
    score = ''

    # start by loading and printing all records from Golfers.txt
    # first load records
    loadRecords(name, score)

    # then --> print/display all records
    displayRecords(name, score)

    # now; start while loop by geting input from user for menu choices
    while choice != 'Q':
        # display menu
        getMenu()

        # get user choice
        choice = str(input('Please make selection:\t--> ')).upper()

        # if this choice is not one of the legal types
        while choice != 'C' and choice != 'A' and choice != 'R' \
                            and choice != 'D' and choice != 'Q':
            choice = str(input("Use C, A, R, D, or Q, please.\t--> ")).upper()


        # (C) make a Change to one of the records
        if choice == 'C':
            # get user input
            searchName = input('\nPlease enter the name of the golfer \
                                \nwhose record you would like to change. \
                                \n\ne.g., Tiger Woods (given name, surname). \
                                \n\n--> ')

            newScore = int(input('\nPlease enter the new score of the golfer \
                                  \nwhose record you would like to change. \
                                  \n\ne.g., a number between 1-150. \
                                  \n\n--> '))

            # validate user input for ints between 1-150
            if newScore <= 1 or newScore >= 150:
                newScore = int(input('\nEnter a number between 1-150: \t--> '))

            # call function to change the records
            changeRecords(name, score, searchName, newScore)

            # assign return bool from function to 'found' as var
            found = changeRecords(name, score, searchName, newScore)

            # if return is False --> let user know it didn't work
            if found != True:
                print('Record unsuccessfully edited to file.')
            else:
                print('Record was successfully edited to file.')


        # (A) Add a record to the file
        elif choice == 'A':
            print("\nYou are going to add a record")

            searchName = input('\nPlease enter the name of the golfer \
                                \nyou would like to add to the record. \
                                \n\ne.g., Tiger Woods (given name, surname). \
                                \n\n--> ')

            lookUpRecords(name, score, searchName)

            # assign return bool from function to 'found' as var
            found = lookUpRecords(name, score, searchName)

            print(type(found))
            print(found)

            # if return is False --> let user know it didn't work
            if found == True:
                print('Name already exists in Records; cannot write to file.')
            else:
                # add name to Golfers.txt
                addRecords(name, score, searchName)

                # make sure name is in file
                lookUpRecords(name, score, searchName)

                # assign return bool from function to 'inFile' as var
                inFile = lookUpRecords(name, score, searchName)

                print(searchName)
                print(type(inFile))
                print(inFile)

                # if return is False --> let user know it didn't work
                if inFile != True:
                    print('Record unsuccessfully added to file.')
                else:
                    print('Record was successfully added to file.')



        # (R) Remove a record from the file
        elif choice == 'R':
            # get user input
            searchName = input('\nPlease enter the name of the golfer \
                                \nwhose record you would like to delete. \
                                \n\ne.g., Tiger Woods (given name, surname). \
                                \n\n--> ')

            # call function to change the records
            removeRecords(name, score, searchName)

            found = removeRecords(name, score, searchName)
            print(searchName)
            print(type(found))
            print(found)
            if found != True:
                print('Record unsuccessfully deleted from file.')
            else:
                print('Record was successfully deleted from file.')


        # (D) Display the file with all records
        elif choice == 'D':
            # load Golfers.txt
            loadRecords(name, score)

            # print/display all records
            displayRecords(name, score)

            found = displayRecords(name, score)

            if found != True:
                print('Record unsuccessfully displayed from file.')
            else:
                print('Record was successfully displayed from file.')


        # (Q) Quit the program
        elif choice == 'Q':
            print('Goodbye.')

# function opens Golfers.txt to 'r' and sends information to dictionary
def loadRecords(k, v):
    # reset dictionary
    records.clear()

    # open the original Golfers.txt file
    infile = open("Golfers.txt", "r")

    # read the first line of Golfers' 'name' field
    k = infile.readline()

    # read rest of file (separating 'name', or 'k', from 'score', or, 'v')
    while k != '':

        # read the score field
        v = infile.readline()

        # strip the '\n' from 'name'
        k = k.rstrip('\n')
        v = v.rstrip('\n')

        # send name and score to dictionary
        records[k] = v

        # read next name and iterate until empty line is reached
        k = infile.readline()

    # close file
    infile.close()

# function only prints all records from Golfers.txt
def displayRecords(name, score):
    # create bool var to use as flag
    found = False

    # title info
    print('Golfers Records:\n')

    # call function to load records
    loadRecords(name, score)

    # print all records
    for (name, score) in records.items():
        print("Golfer's Name: ", name, "\t\tGolfer's Score: ", score)
        found = True

    # If search value was not found in file, return False
    if found:
        return True
    else:
        return False

# function for searching records
def lookUpRecords(name, score, searchName):
    # create bool var to use as flag
    found = False

    # second, need to load the Golfers.txt file to update records
    loadRecords(name, score)

    # then, set 'search' var to 'get' info from dictionary to avoid
    # runtime error --> 0 is set to return it instead of 'none'
    search = records.get(searchName, 0)

    # determine if 'name' was found or not; '0' is the value returned from
    # records.get(variable, 0)
    if search != 0:
        print('Name found in Records.')
        found = True
    else:
        print('Name not found in Records.')

    # If search value was not found in file, return False
    if found:
        return True
    else:
        return False

# add records to file--use other functions to build
def addRecords(name, score, searchName):
    # first; open in 'a' mode to add information
    infile = open("Golfers.txt", "a")

    # use the name the user inputed in main to add to file
    name = searchName
    # make sure the score is entered as 'int'
    score = int(input("Enter the golfer's score:\n--> "))

    # validate user input for ints between 1-150
    if score <= 1 or score >= 150:
        score = int(input('\nEnter a number between 1-150: \t--> '))

    # append to the file
    print('Writing to file...\n...\n...\n...')
    infile.write(name + '\n')
    infile.write(str(score) + '\n')
    print('File successfully written.')

def removeRecords(name, score, searchName):
    # create bool var to use as flag
    found = False

    # open the original Golfers.txt file
    infile = open("Golfers.txt", "r")

    # open the temp file
    outfile = open("Temp.txt", "w")

    # read the first record's 'name' field
    name = infile.readline()

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name'
        name = name.rstrip('\n')

        # strip the '\n' from 'score'
        score = score.rstrip('\n')

        # search determins if user input is written to Golfer's file, or temp
        if name == searchName:
            # reset dictionary
            # records.clear()
            # set found flag to true
            found = True
        else:
            # write original score to temp file
            outfile.write(name + '\n')
            outfile.write(str(score) + '\n')

        # read next name
        name = infile.readline()

    # Close Golfers.txt file + Temp.txt file
    infile.close()
    outfile.close()

    # Delete original Golfers.txt file
    os.remove('Golfers.txt')

    # Rename Temp.txt file
    os.rename('Temp.txt', 'Golfers.txt')

    # If search value was not found in file, return False
    if found:
        return True
    else:
        return False


def changeRecords(name, score, searchName, newScore):
    # create bool var to use as flag
    found = False

    # open the original Golfers.txt file
    infile = open("Golfers.txt", "r")

    # open the temp file
    outfile = open("Temp.txt", "w")

    # read the first record's 'name' field
    name = infile.readline()

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name'
        name = name.rstrip('\n')

        # strip the '\n' from 'score'
        score = score.rstrip('\n')

        # search determins if user input is written to Golfer's file, or temp
        if name == searchName:
            outfile.write(name + '\n')
            outfile.write(str(newScore) + '\n')

            # set found flag to true
            found = True
        else:
            # write original score to temp file
            outfile.write(name + '\n')
            outfile.write(str(score) + '\n')

        # read next name
        name = infile.readline()

    # Close Golfers.txt file + Temp.txt file
    infile.close()
    outfile.close()

    # Delete original Golfers.txt file
    os.remove('Golfers.txt')

    # Rename Temp.txt file
    os.rename('Temp.txt', 'Golfers.txt')

    # If search value was not found in file, return False
    if found:
        return True
    else:
        return False

# function to print the menu
def getMenu():
    print('Please make a selection from the Menu below:\
          \n\t(C) make a Change to one of the records\
          \n\t(A) Add a record to the file\
          \n\t(R) Remove a record from the file\
          \n\t(D) Display the file with all records\
          \n\t(Q) Quit the program')

# call the main function
main()
