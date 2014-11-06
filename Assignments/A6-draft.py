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

      hints: -->read from 'Golfers.txt'; write to 'temp'; rename 'temp'
                'Golfers.txt'
             -->pages


"""
# need to remove and rename files
import os

# main function
def main():
    # local variable
    choice = ''
    found = ''

    # start by printing all records from Golfers.txt
    showRecord()

    # get input from user
    while choice != 'Q':
        # display menu
        getMenu()

        # get user choice
        choice = str(input('please make selection:\t--> ')).upper()

        # this letter is not one of the legal types
        while choice != 'C' and letter != 'A' and letter != 'R' \
              and letter != 'D' and letter != 'Q':
            choice = str(input("Use C, A, R, D, or Q, please.\t--> ")).upper()

        if choice == 'C':
            # get the search value and new score
            search = input("Enter the Golfer's name you are looking for: ")
            newScore = int(input('Enter the updated score: '))

            # validate user input for ints between 1-150
            if newScore <= 1 or newScore >= 150:
                newScore = int(input('Enter a number between 1-150: '))

            # send search, newScore, + err to changeRecord()
            changeRecord(search, newScore, found)

            # determin if there is an I/O error

            if found == True:
                print('Name found and successfully written to file')
            elif found == False:
                try:
                    showRecord()
                    search = input("Are you sure you have the correct name \
                                    of the Golfer you are looking for? \
                                    \nuse the record above as a reference \
                                    \nEnter the Golfer's name you are looking \
                                    for: \t--> ")
                    break
                except ValueError:
                    print("Oops!  That is not a correct Golfer's name!")

        elif choice == 'A':
            # add new record to the file
            print("Enter a new golfer's name and their score:")
            newName = input('\n\tName: \t--> ')
            newScore = int(input('\n\tScore: \t--> '))

            # validate user input for ints between 1-150
            if newScore <= 1 or newScore >= 150:
                newScore = int(input('\nEnter a number between 1-150: \t--> '))

            # send name, score, + err to addRecord()
            addRecord(newName, newScore, found)

"""
--> for C:
      ask for name of golfer
      ask for new score
      validate
      send info to changeRecord(searchName, score) function
      if no match is found, write to temp file + return false to main
      if name is found, write to file + return true to main
      main() lets user know if they were successful or not
      (use a try/except statement looking for the IOError)
"""
# menu selection 'C' modifies a record
# --> needs to return 'bool'
def changeRecord(search, newScore, found):
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

        # search determins if user input is written to Golfer's file, or temp
        if name == search:
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
        return False
    else:
        return True

"""
--> for A:
      give name of new golfer + score
      validate
      send to addRecord(name, score) where it will append the data file
      return true if sucessful; false if not
      main() lets user know if they were successful or not
      (use a try/except statement looking for the IOError)
"""
# menu selection 'A' adds a record to file
# --> needs to return 'bool'
def addRecord(newName, newScore, found):
    # first, need to search record to preven duplicate records
    # create bool var to use as flag
    found = False

    # open the original Golfers.txt file
    infile = open("Golfers.txt", "r")

    # read the first record's 'name' field
    name = infile.readline()

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name'
        name = name.rstrip('\n')

        # search determins if user input is written to Golfer's file, or temp
        if name == search:
            print('There is already a record for this golfer.')

            # set found flag to true
            found = False
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
        return False
    else:
        return True





"""
-->  for R:
      give name of golfer to remove
      send to removeRecord(searchName)
      if name not found return false
      main() lets user know if they were successful or not
      (use a try/except statement looking for the IOError)
"""
# menu selection 'R' removes a record from file
# --> needs to return 'bool'
def removeRecord():
    ...

"""
-->  for D:
      display records from Golfers.txt file
      return true when complete
      main() lets user know if they were successful or not
      (use a try/except statement looking for the IOError)
"""
# menu selection 'D' shows user the file
def showRecord():
    # open the original Golfers.txt file to print all records
    infile = open("Golfers.txt", "r")

    # read the first record's 'name' field
    name = infile.readline()

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name'
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        # print all records from Golfers.txt
        print('Name of Golfer: ', name, '\t\tScore: ', score)

        # read next name
        name = infile.readline()

    # Close Golfers.txt file
    infile.close()

# User menu
def getMenu():
  print('Please make a selection from the Menu below:\
        \n\t(C) make a Change to one of the records\
        \n\t(A) Add a record to the file\
        \n\t(R) Remove a record from the file\
        \n\t(D) Display the file with all records\
        \n\t(Q) Quit the program')

"""
-->  for Q:
      End program--data file must be closed before ending the program
"""
# menu selection 'Q' quits program (likely needs to be in main())

# call main function
main()
