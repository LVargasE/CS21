"""
A7 -- World Series Champions

To-Do:

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
    noDuplicates(winners)
    #print(winnersND)  
    numberWins()
    winsTuple = numberWins()
    # print(winsTuple)
    # pretend append tuple
    try:
        winsTuple.append()
    except AttributeError: 
        print('Tuples cannot be changed--error')
    
    createFileNoDuplicates(winsTuple)
    # Print all winners from US Presidential Election Years
    print('\nWins on US Presidental Elections')
    # Reload winners data
    winners = readData()
    # use index to control for loop
    index = 0
    # if the index matches the years already determined to be election years,
    # print that item
    for item in winners:
        # accumulator 
        index += 1
        # index slice of all the presidental election years
        if index == 5 or index == 9 or index == 13 or index == 17 \
            or index == 21 or index == 25 or index == 29 or index == 33 \
            or index == 37 or index == 41 or index == 45 or index == 49 \
            or index == 53 or index == 57 or index == 61 or index == 65 \
            or index == 69 or index == 73 or index == 77 or index == 81 \
            or index == 85 or index == 89:
                print(item)
    
    
    
    
    
    

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
def noDuplicates(theList):
    # use blank dictionary to store found values from list
    found = {}
    # use an accumulator pattern + for--> if loop to remove duplicates
    index = 0
    # for every iteration of an element in theList --> if not already found,
    # delete element at its indexed number (arrived at through the 
    # accumulator pattern with variable 'index')
    for item in theList:
        if item not in found:
            found[item] = True
            theList[index] = item
            # accumulator
            index += 1
    # delete element from list
    del theList[index:]
    
    # convert list to tuple
    theList = tuple(theList)
    # return tuple-ized list
    return theList
 
# calculate number of wins   
def numberWins():
    # ...
    theList = readData()    
    index = 0
    winnersList = []
    for item in theList:
        counter = theList.count(item)
        winnersList.append(counter)
        winnersList[index] = str(counter) + '\t' + item
        index += 1
    
    noDuplicates(winnersList)
    print(winnersList)
    winnersList = tuple(winnersList)
    return winnersList
    
def createFileNoDuplicates(aTuple):
    # 
    index = 0
    outfile = open("WorldSeriesWinnersND.txt", "w")
    try:
        for item in aTuple:
            #
            outfile.write(item + '\n')
            #
            index += 1
    except IOError:
        print("Something happenned when trying to write to the file!")
    finally:
        outfile.close()
    print('\nThe following is data you have saved to the file:\n')
    index = 0
    for item in aTuple:
        print(item)
        index += 1
    
# excecute the main() function !
main()
