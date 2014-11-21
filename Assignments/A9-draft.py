"""
The Program Spec:

Use the same value-returning function as before named readData() that will use
a try/except statement to read in the data from the file named above, remove
the end line characters, and put all of the winners in a list.  Check for an
IOError.  Return the list to the main.

Next, design a function named makeDictionaries( winners ) that receives the
list of winners and creates two Dictionaries, yearD and winsD. The first one
has the year as the key and the team as the value.  The second will have the
team as the key and the number of wins as the value.  Make sure that you do
NOT put the years 1904 and 1994 in the Dictionary.  Start at the base year of
1903 and use the combination of For and If to do this. The wins dictionary can
be created in the same loop by checking to see if the team is in the wins
dictionary already and updating the number of wins.  Next return both the
yearD and winsD to the main at the same time (pg 224).

Now we can move onto a function named noDuplicates( yearD ) that receives the
dictionary with the years linked to teams and creates a set of winners that is
by definition, non-duplcated.  Use the For loop for sets and add each one.
Now just return it to the main.

Create a function named createFileNoDuplicates( winsD ) that receives the
dictionary with the teams linked to wins and Pickles the data so that it can
be written out to the file WorldSeriesWinnersND2.txt in the binary format.
Be sure to put the writing to the file in a try/except block that will catch
an IOError.  Be sure to close the file after you are done writing.  It may
look like the program will work without it but the file does not always close
properly with you doing it explicitly.  Not doing so will result in a loss of
points.

The main() should call:
  readData()
  makeDictionaries( winners )
  noDuplicates( yearD )

Next print out the non-duplicated winners to the screen (remember that they
could be in any order).  Then call createFileNoDuplicates( winsD ) to create
the new file.

- As a last item for the main(), have the user enter a year in the range of
1903 - 2008.  Validate that the input is only digits and is in the range.
(You can use an infinite loop and break out when everything is good.  Make
sure you can handle the user entering an out of range number and then a
non-digit after that.)  If they chose 1904 or 1994 then tell them that there
was no World Series that year and end.  If they chose a good year, then show
the team that won it and the number of times that they have won it.

Be sure to include comments in your code.

Create a run and include it as output with your program. As an exception this 
time, include the WorldSeriesWinnersND2.txt file as a second file submission.
"""
def main():
    
    winners = readData()
    
    makeDictionaries(winners)
    
def readData():
    aList = []
    
    try:
        # Open the file for reading
        inputFile = open('WorldSeriesWinners2.txt', 'r')
        # Read all the lines in file into a list
        aList = inputFile.readlines()
        # Strip trailing newline characters
        for i in range(len(aList)):
            aList[i] = aList[i].rstrip(" \n")

        inputFile.close()
        
    # if there is an IOError, show it
    except IOError:
        print("The file could not be found")

    # return the list to the main
    return aList
    
def makeDictionaries(aList):
    # has the year as the key and the team as the value
    year = {}
    # has the team as the key and the number of wins as the value
    wins = {}
    
    for k in aList:
        
    
    return year, wins
    
def noDuplicates(yearD):
    ...
    
# call main function
main()
