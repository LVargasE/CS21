"""
A7 -- World Series Champions

To-Do:

  * Create a value-returning function named numberWins( winners, winnersND )
    that receives the list of winners and the tuple of non-duplcated winners
    (winnersND). Create a new list that will hold the number of wins for each
    team in the winnersND tuple.  (The wins list indexes should match the
    winnersND indexes, meaning that index 3 of the winnersND tuple should have
    the number of wins in the index 3 of the wins list.)
    Use a combination of nested For loops and If's to do this.  After the new
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
noDuplicates(winners)
numberWins(winners, winnersND)
createFileNoDuplicates(NoDupTuple, winsTuple)
"""
def main():
    winners = readData()
    #print(winners)
    winnersND = noDuplicates(winners)
    #print(winnersND)
    numberWins(winners, winnersND)
    

# read the data from .txt file and pass it to main() as list without '\n'
def readData():
    # in case of an IOError; use try, except, else
    try:
        # open file to read assigned to 'infile'
        infile = open('WorldSeriesWinners.txt', 'r')
    # unless there's an IOError; then print message
    except IOError:
        print('Something happenned when trying to read the file!')
    # if everything was read without an error, remove new line from strings
    else:
        # variable that represents list from file
        alist = infile.readlines()
        # close the file
        infile.close()
    # use an accumulator pattern + while loop to remove '\n' from strings    
    index = 0
    # so long as the accumulated number is less than the len of the list -->
    while index < len(alist):
        # as the slice number changes, it moves through the list removing '\n'
        alist[index] = alist[index].rstrip('\n')
        # accumulator
        index += 1
    # return the list to main()
    return alist

# ...
def noDuplicates(thelist):
    # use blank dictionary to store found values from list
    found = {}
    # use an accumulator pattern + for--> if loop to remove duplicates
    index = 0
    # for every iteration of an element in thelist --> if not already found,
    # delete element at its indexed number (arrived at through the 
    # accumulator pattern with variable 'index')
    for item in thelist:
        if item not in found:
            found[item] = True
            thelist[index] = item
            # accumulator
            index += 1
    # delete element from list
    del thelist[index:]
    
    # convert list to tuple
    thelist = tuple(thelist)
    # return tuple-ized list
    return thelist
 
# ...   
def numberWins(k_winners, v_winnersND):
    
    
# excecute the main() function !
main()
