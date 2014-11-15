"""
A7 -- World Series Champions

"""
# define the main program
def main():
    # load data and assign list to winners variable
    winners = readData()
    # pass the list to a function that will remove duplicates
    noDuplicates(winners)
    # calculate number of wins and return a nonduplicate tuple with wins +
    # teams
    numberWins()
    # assign the results of previous function to variable
    winsTuple = numberWins()
    # pretend append tuple
    try:
        winsTuple.append()
    except AttributeError: 
        print('Tuples cannot be changed--error')
    # write the winsTuple to a new file
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

# remove duplicates
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
    # reload data and assign list to 'theList' variable 
    theList = readData()  
    # use to control for loop
    index = 0
    # blank list to send wins to
    winnersList = []
    for item in theList:
        # do it all at once; search for number of wins
        counter = theList.count(item)
        # append data to winnersList
        winnersList.append(counter)
        # combine number of wins, convert to string, at a tab, and concatenate
        # with team string
        winnersList[index] = str(counter) + '\t' + item
        # accumulator
        index += 1
    # remove duplicates
    noDuplicates(winnersList)
    # convert to tuple
    winnersList = tuple(winnersList)
    # return tuple to main()
    return winnersList

# write tuple to file    
def createFileNoDuplicates(aTuple):
    # control for loop in 'try'
    index = 0
    # open file to write and create if file doesn't exist
    outfile = open("WorldSeriesWinnersND.txt", "w")
    # anticipate IOError
    try:
        for item in aTuple:
            # write to file with new line
            outfile.write(item + '\n')
            # accumulator 
            index += 1
    # if there's an IOError, then -->
    except IOError:
        print("Something happenned when trying to write to the file!")
    # make sure no matter what the file closes
    finally:
        outfile.close()
    # show user what was printed to file
    print('\nThe following is data you have saved to the file:\n')
    # use the for loop to make it easier
    index = 0
    for item in aTuple:
        print(item)
        index += 1
    
# excecute the main() function !
main()
