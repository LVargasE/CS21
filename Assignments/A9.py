"""
A9--World Series 
--> read data from file, convert to two dictionaries, + remove duplicates
--> pickle data (serialize) to file in binary
--> ask user to select a year + tell user which team won the World Series that year (if played)

"""
import pickle
def main():
    # local variable to control user input loop
    endProgram = 0
    
    # assign variable to the function that reads the data and returns list from file
    winners = readData()
        
    # assign the two returned dictionaries from function to two variables
    yearD, winsD = makeDictionaries(winners)
        
    # print only the teams (keys) from the winsD dictionary        
    for aKey in winsD.keys():
        print(aKey)
        
    # create new dictionary variable for the non-duplicated yearD dictionary
    yearDictND = noDuplicates(yearD)   
    
    # serialize/pickle the data
    createFileNoDuplicates(winsD)
    
    # user input loop for program
    while endProgram != 1:
        
        # user input assigned variable 'choice' to control loop with flag 'endProgram'
        choice = input('Enter a year in the range 1903-2008:\n-->  ')
                   
        while True:            
            try:
                # user input assigned variable 'choice' to control loop with flag 'endProgram'
                choice = int(input('You must enter a year between 1903-2008 \
                                             (use four digits for year; e.g., 1955)\n-->  '))
            except ValueError:
                print("Error.  You must enter a year between 1903-2008 \
                         (use four digits for year; e.g., 1955).")
            finally:
                if choice in range(1903, 2009):
                    break
        
        # if choice is a valid selection, use variable 'search' and dictionary method .items()
        # to run through the Year no-dups dictionary to display the info the user wants
        if choice >= 1903 and choice <= 2008:
            search = yearDictND.items()
            for (aTeam, yearList) in search:
                if choice in yearList:
                    print('The team that won the World Series in', choice, 'is the', aTeam, '; \n\
                             they won', len(yearList), 'time(s) between 1903 and 2008.')
        
        # if the user selects the two years the world series didn't happen, they get the boot
        elif choice == 1904 or choice == 1994:
            print('There was no World Series played that year')
            endProgram = 1
        elif choice not in range(1903, 2009):
            print('The data for year', choice, 'is not included in our database.')
        
        # find out if the user wants to look up any other years
        quit = str(input("Quit the program?  ('Y' or 'N')\n--> ")).lower()
        if quit == 'yes' or quit == 'y':
            endProgram = 1
        elif quit == 'no' or quit == 'n':
            print("\nLet's continue!\n")
        # validation isn't as important here; if they don't follow directions they will continue!
        else:
            print("Answers must be either: 'Y' or 'Yes'; or, 'N' or 'No'.")


# function to read the data from .txt file and return to main as a list  
def readData():
    aList = []
    
    # make sure there isn't an error
    try:
        # open the file for reading
        infile = open('WorldSeriesWinners2.txt', 'r')
        # read all the lines in file into a list
        aList = infile.readlines()
        # strip trailing newline characters
        for index in range(len(aList)):
            aList[index] = aList[index].rstrip(" \n")
        
        # close the file
        infile.close()
        
    # if there is an IOError, show it
    except IOError:
        print("The file could not be found")

    # return the list to the main
    return aList
 
# create two separate dictionaries from the list and return both to the main   
def makeDictionaries(aList):
    # has the year as the key and the team as the value
    yearD = {}
    # has the team as the key and the number of wins as the value
    winsD = {}
    # index control variable for the years data to extract from list
    yearIDX = 0
    # index control variable for the wins data to extract from list
    winsIDX = 0
    
    # for loop to extract the years from list
    for year in range(1903, 2009):
        # don't add the two years the game wasn't played
        if year == 1904 or year == 1994:
            pass
        else:
            # add to dictionary
            yearD[year] = aList[yearIDX]
        
        # accumulate
        yearIDX += 1
    
    # for loop to extract the teams/wins from list
    for aTeam in aList:
        aTeam = aList[winsIDX]
        # don't add data for the year that wasn't played
        if 'Not Played' in aTeam:
            pass
        # add to the value of a key-value pair already in dictionary        
        elif aTeam in winsD:
            winsD[aTeam] = winsD[aTeam] + 1
        # add the key and value to dictionary
        else:       
            winsD[aTeam] = 1
        
        # accumulate
        winsIDX += 1
        
    # return both the years + wins dictionaries to main
    return yearD, winsD

# remove the duplicates from the years dictionary    
def noDuplicates(aDict):
    # temp dictionary to separate duplicates    
    dictND = {}
    
    # for loop to sift through keys and values in the dictionary
    for (aYear, aTeam) in aDict.items():
        # if team already in non-dup dictionary; add the year to a nested list as a value        
        if aTeam in dictND:
            dictND[aTeam] += [aYear]
        # otherwise; add the key and value to non-dup dictionary
        else:
            dictND[aTeam] = [aYear]
            
    # return non-dup dictionary
    return dictND
 
# pickle/serialize the data!   
def createFileNoDuplicates(aDict):
    try:
        # open the file for writing to file in binary
        outfile = open('WorldSeriesWinnersND2.txt', 'wb')
        
        # pickle the dictionary
        pickle.dump(aDict, outfile)        
        
        # close the file
        outfile.close()
        
    # if there is an IOError, show it
    except IOError:
        print("Something happenned while writing to file!")
    
# call main function
main()
