"""
A5 --> Golf Scores/Statistics

 Use file to save/update Golf Scores

 program specs
 -->  Display all records in the file, then enter user-input
      loop with a 5 value menu at each pass of the loop (use a function)
 -->  User enters single letter only (use validation)
 -->  The user can change one of the records (C), add a record to the file (A),
      remove a record from the file (R), display all the records (D), or
      quit (Q).





 -->  Always validate user input
 -->  Don't need to test for non-numeric values when user asked to enter numbers
 -->  Submit a run that shows everything with several passes of the loop
      all choices must be used twice in random order (except Q)--show one
      illegal choice/bad choice

      hints: -->read from 'Golfers.txt'; write to 'temp'; rename 'temp'
                'Golfers.txt'
             -->pages


"""
# main
def main():
    # open Golfers.txt to read to
    infile = open("Golfers.txt", "r")
    # create + open a temp file for user input
    outfile = open("Temp.txt", "w")

    name = infile.readline()

    while name != '':
        score = int(infile.readline())

        name = name.rstrip('\n')



    for aline in infile:
        values = aline.split(2) # not sure the 2 will work
        print('Golfer's Name: ', values[0], 'had a score of ')



    infile.close()

    outfile.close()


"""
--> for C:
      ask for name of golfer
      ask for new score
      validate
      send info to changeRecord(searchName, score) function
      if no match is found, write to temp file + return true to main
      if name is not found, return false to main
      main() lets user know if they were successful or not
      (use a try/except statement looking for the IOError)
"""
# menu selection 'C' modifies a record
# --> needs to return 'bool'
def changeRecord():
    # create bool var to use as flag
    found = False

    # get the search value and new score
    search = input("Enter the Golfer's name you are looking for: ")
    newScore = int(input('Enter the updated score: '))

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

    # Close Golfers.txt file

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
def addRecord():
    ...

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
    ...

"""
-->  for Q:
      End program--data file must be closed before ending the program
"""
# menu selection 'Q' quits program (likely needs to be in main())
