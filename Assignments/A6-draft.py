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
      --> for C:
            ask for name of golfer
            ask for new score
            validate
            send info to changeRecord(searchName, score) function
            if no match is found, write to temp file + return true to main
            if name is not found, return false to main
            main() lets user know if they were successful or not
            (use a try/except statement looking for the IOError)
      --> for A:
            give name of new golfer + score
            validate
            send to addRecord(name, score) where it will append the data file
            return true if sucessful; false if not
            main() lets user know if they were successful or not
            (use a try/except statement looking for the IOError)
      -->  for R:
            give name of golfer to remove
            send to removeRecord(searchName)
            if name not found return false
            main() lets user know if they were successful or not
            (use a try/except statement looking for the IOError)
      -->  for D:
            display records from Golfers.txt file
            return true when complete
            main() lets user know if they were successful or not
            (use a try/except statement looking for the IOError)
      -->  for Q:
            End program--data file must be closed before ending the program
 -->  Always validate user input
 -->  Don't need to test for non-numeric values when user asked to enter numbers
 -->  Submit a run that shows everything with several passes of the loop
      all choices must be used twice in random order (except Q)--show one
      illegal choice/bad choice

      hints: -->read from 'Golfers.txt'; write to 'temp'; rename 'temp'
                'Golfers.txt'
             -->pages


"""

infile = open("Golfers.txt", "r")
outfile = open("Golfers.txt", "w")

aline = infile.readline()

for aline in infile:
    values = aline.split(2) # not sure the 2 will work
    print('Golfer's Name: ', values[0], 'had a score of ')



infile.close()
outfile.close()
