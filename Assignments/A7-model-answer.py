'''
Assignment 7
CS 21A
Instructor Solution
'''

def main():
    # call the function to read in the data from the file
    winners = readData()

    # Capture the created noDuplicates tuple
    winnersNoDupTuple = noDuplicates(winners)

    # capture the created wins tuple
    numWinsTuple = numberWins(winners, winnersNoDupTuple)

    # attempt to append a tuple and show the error
    try:
        numWinsTuple.append(4)
    except:
        print("Cannot append tuples")

    # Create the file that has no duplicates and the number of wins
    createFileNoDuplicates(winnersNoDupTuple, numWinsTuple)

    # print out the list of non-duplicated winners and their number of wins
    print("\n")
    print("Winning teams and their number of wins\n")
    for i in range(len(winnersNoDupTuple)):
        print(numWinsTuple[i], "\t", winnersNoDupTuple[i],"\n")

    # print out the winning team for each election year
    print("\nWinning Teams each presidential year from 1908-1992")
    for team in winners[4:89:4]:
        print(team)

# end main()



# read in all of the data from the file into a list
def readData():
    winners = []
    
    try:
        # Open the file for reading
        inputFile = open('WorldSeriesWinners.txt', 'r')
        # Read all the lines in file into a list
        winners = inputFile.readlines()
        # Strip trailing newline characters
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip(" \n")

        inputFile.close()
        
    # if there is an IOError, show it
    except IOError:
        print("The file could not be found")

    # return the list to the main
    return winners

# end readData()


# create a list of winners with no duplicates
def noDuplicates(winners):    
    # create a blank list
    winnersND = []

    # for each winner in the list, add the winner to the NoDup list if it is
    #   not in there already    
    for i in range(len(winners)):
        if winners[i] not in winnersND:
            winnersND.append(winners[i])
    # end For

    # convert the list to a tuple so it cannot be changed
    NoDupTuple = tuple(winnersND)

    # return the tuple
    return NoDupTuple

# end noDuplicates()



# Create a list that has the corrosponding number of wins for each
#   team that is listed in the NoDup list
def numberWins(winners, winnersND):       
    # create a blank wins list
    wins = []

    # for each winner in the non-duplicated list, see how many times the team
    #   shows up in the original winners list
    for i in range(len(winnersND)):
        wins.append(0)
        teamNoDup = winnersND[i]
        for teamWin in winners:
            if teamNoDup == teamWin:
                wins[i] += 1
        # end For
    # end For    

    # convert the list to a tuple so it cannot be changed
    winsTuple = tuple(wins)

    # return the tuple
    return winsTuple

# end numberWins()




# create a new output file with the non-duplicated winners and their number of wins
def createFileNoDuplicates(noDupTuple, winsTuple):
    try:
        # Open the file for writing
        outFile = open('WorldSeriesWinnersND.txt', 'w')
        # Write out NoDup tuple with Wins tuple
        for i in range(len(noDupTuple)):
            outFile.write(str(winsTuple[i]) + '\t' + noDupTuple[i] + '\n')

        outFile.close()
        
    except IOError:
        print("The file could not be created")

# end createFileNoDuplicates()

    


# call the main function
main()