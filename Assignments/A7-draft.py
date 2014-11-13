"""
A7 -- World Series Champions

To-Do:

  * Create a value-returning function named readData() that will use a
    try/except statement to read in the data from the file named above, remove
    the end line characters, and put all of the winners in a list.  Check for
    an IOError.  Return the list to the main.

  * Create a value-returning function named noDuplicates( winners ) that
    receives the list of winners and creates a new list of non-duplicate
    winners.  This can be done by going through the list of winners and
    appending a team to the new list every time it does NOT appear in the new
    list so far.  Use the combination of For and If to do this.  After the new
    list of non-duplicate winners is created, convert it to a tuple so that it
    cannot be changed any time later.  Next return the tuple to the main.

  * Create a value-returning function named numberWins( winners, winnersND )
    that receives the list of winners and the tuple of non-duplcated winners
    (winnersND). Create a new list that will hold the number of wins for each
    team in the winnersND tuple.  (The wins list indexes should match the
    winnersND indexes, meaning that index 3 of the winnersND tuple should have
    the number of wins in the index 3 of the wins list.)
  * Use a combination of nested For loops and If's to do this.  After the new
    list of wins is created, convert it to a tuple so that it cannot be changed
    any time later.  Next return the tuple to the main.

  * Create a function named createFileNoDuplicates( noDupTuple, winsTuple )
    that receives the two above created tuples and prints them out to a file.
    Each line of the file should have the number of wins for a team, a tab, and
    then the name of the team.  The file should be called
    WorldSeriesWinnersND.txt and its writing should be inside of a try/except
    block that will catch an IOError.  Be sure to close the file after you are
    done writing.  It may look like the program will work without it but the
    file does not always close properly with you doing it explicitly.  Not
    doing so will result in a loss of points.

  * The main() should call readData(), noDuplicates( winners ), and
    numberWins( winners, winnersND ).  Then attempt to append something to the
    wins tuple and print out the error that is caught using a try/except block.
    Then call createFileNoDuplicates( NoDupTuple, winsTuple )  to print the new
    file.  Now print to the screen the same list that was just saved to the
    file.
  * As a last item for the main() use List Slicing to print out each team that
    won the World Series in each election year starting in 1908 and continuing
    to 1992 using the original winners list.  (hint: 1) Don't forget that there
    was no Series in 1904.  2) figure out which spot in the list is the
    year 1992)

  * Be sure to include comments in your code.

  * Create a run and include it as output with your program. As an exception
    this time, include the WorldSeriesWinnersND.txt file as a second file
    submission.

main()
readData()
noDuplicates( winners )
numberWins( winners, winnersND )
createFileNoDuplicates( NoDupTuple, winsTuple )
"""
def main():
    winnersList = []
    winners = ''
    index = 0
    readData(winners)
    print(winners)


def readData():
    # open the text document and assign to 'infile'
    infile = open("WorldSeriesWinners.txt", "r")

    # read the first line of Golfers' 'name' field
    k = infile.readline()

    # read rest of file (separating 'name', or 'k', from 'score', or, 'v')
    while k != '':

        # strip the '\n' from 'line'
        k = k.rstrip('\n')

        # send name of team to winner's list
        winnersList = [k]

        # read next name and iterate until empty line is reached
        k = infile.readline()

    # close file
    infile.close()

    return winnersList

main()
