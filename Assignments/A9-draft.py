"""
The Program Spec:

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
import pickle
def main():
    
    winners = readData()
    # print(winners)
    yearD, winsD = makeDictionaries(winners)
    for aKey in winsD.keys():
        print(aKey)
    # print(yearD)
    # print(winsD)
    # print(len(yearD))
    # print(len(winsD))
    
    yearDictND = noDuplicates(yearD)
    # print(yearDictND)
    createFileNoDuplicates(winsD)
    
    flag = False
    while flag != True:
        try:
            choice = int(input('Enter a year in the range 1903-2008: '))
        except ValueError:
            choice = int(input('Only numbers are accepted.\n \
                                       Enter a year in the range 1903-2008: '))

    if choice == 1904 or choice == 1994:
        print('There was no World Series played that year')
        flag = True
    elif choice <= 1904 or choice >= 2008:
        print('The data for year', choice, 'is not included in our database')
    elif choice >= 1904 or choice <= 2008:
        for (k, v) in yearDictND.items():
            if choice in k:
                print('The team that won the World Series in', choice, 'is the', \
                         v, '.\nThey won', len(k), 'times.\n')
                flag = True
            else:
                print('Your entry: ', choice, '; was not found in the records--an error \
                         has occurred')
    
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
    yearD = {}
    # has the team as the key and the number of wins as the value
    winsD = {}
    yearIDX = 0
    winsIDX = 0
    
    for year in range(1903, 2009):
        if year == 1904 or year == 1994:
            pass
        else:
            # add to dictionary
            yearD[year] = aList[yearIDX]
        yearIDX += 1
    
    for aTeam in aList:
        aTeam = aList[winsIDX]
        if 'Not Played' in aTeam:
            pass
        elif aTeam in winsD:
            winsD[aTeam] = winsD[aTeam] + 1
        else:
            # add to dictionary       
            winsD[aTeam] = 1
        winsIDX += 1
        
    # return both the years + wins dictionaries
    return yearD, winsD
    
def noDuplicates(aDict):
    dictND = {}
    
    for (aYear, aTeam) in aDict.items():
        if aTeam in dictND:
            dictND[aTeam] += [aYear]
        else:
            dictND[aTeam] = [aYear]
            

    return dictND
    
def createFileNoDuplicates(aDict):
    try:
        # open the file forreading
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
