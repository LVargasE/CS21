"""
A8--Word Games

Change user input string into pig latin and turkey irish

The Program Spec

    Ask the user to enter a target string ( minimum of 3 words).  Be sure to use
    validation to make sure the minimum is reached.  Then, show the user three
    things:

    The target string with the Pig Latin change.
    The target string with the Turkey Irish change.
    The number of vowels in the target string.
    All of the displays of the above 3 things are done from the main().

    Have the program loop for a total of 3 times asking the user for a string each
    time.

    Input function

 -->getString()

    This function requests a string from the user and converts it to a list to
    be able to see how many words were entered.  Use a validation loop to get the
    minimum of 3 words. Return the targetList to the main()



    Processing functions

 -->pigLatin( targetList )

    This function will receive the list of words as an argument and returns a
    new string that has moved the first letter to the end and added "ay" to each
    word in the targetList. Start by making each word all lower case for
    consistency.  Consider slicing the word to get certain parts and then create
    the new string.

 -->turkeyIrish( targetList )

    This function will receive the list of words as an argument and returns a
    new string that has "ab" added before each vowel in each word. Start by making
    each word all lower case for ease in searching for vowels ('a', 'e', 'i',
    'o', 'u') in the words.  Think about how look at each letter and then add
    to the new string.

 -->countVowels( targetList )

    This function will receive the list of words as an argument and returns the
    number of vowels that appear in the list of words.  Check for 'a', 'e', 'i',
    'o', 'u'.  Again think about making the words lower case to help with the
    search.

    Input Errors

    Whenever the user makes an input error, keep at them until they get it right.
    Do not allow them out of the validation loop until you have acquired a legal
    value, even if it takes years
    
Use the following functions:
    main()
    getString()
    pigLatin( targetList )
    turkeyIrish( targetList )
    countVowels( targetList )
    
"""
def main():
    # local variables
    ans = 'yes'
    
    print('/nChange a few words into Pig Latin, Turkey Irish, and count \
           all vowels in a sentance of your choosing with Python!')
           
    while ans == 'y' or ans == 'yes':      
        # test the string to list code
        targetList = getString()
        print(getString)
        # test the list to vouwel count code
        vouwelsNumber = countVouwels(targetList)   
        print(vouwelsNumber)
        
        ans = str(input('Would you like to translate another \
                        sentence?\n--> ')).lower()

        

def getString():
    # local variables
    flag = False
    
    while flag != True:
        # ask the user to enter a string
        aString = str(input('\nNEW WORD SET\nEnter a sentance below. \
                              (Please note that sentances must contain at least\
                              three words). \
                              \nEnter string here:--> ')).lower()
     
        # use split method to convert string into a separated list
        splitString = aString.split()
        
        if len(splitString) >= 3:
            # return the value as a list                             
            flag = True
        else:
            #
            print('\nSENTENCE MUST CONTAIN AT LEAST THREE WORDS')
    
    return splitString
    
#
def pigLatin(aList):
    index = 0
    vowels = "aeiou"
    aString = ' '.join(aList)
    while index < len(aString) and (not aString[index] in vowels):
        index += 1
    
    if index == 0:
        print(aString + 'ay')
    elif index < len(aString):
        print(aString[index:] + aString[:index] + 'ay')
    else:
        print(aString)
    return aString
        
#
def turkeyIrish(targetList):
    ...

#
def countVouwels(targetList):
    # list of vowels to look for
    vowels = "aeiou"
    noVowels = ""
    for eachWord in targetList:
        if eachWord in vowels:
            noVowels = noVowels + eachWord
    return noVowels

# call the main function    
main()          