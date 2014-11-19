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
    choice = 'y'
    
    
    print("Change a few words into Pig Latin, Turkey Irish, and count \
           all vowels in a sentance of your choosing with Python!")
                      
    #                
    while choice == 'y':    
        
        # get string from user using the function below:
        getString()                
        
        # assign returned value of function to a variable
        targetList = getString()
    
        try:
            #
            choice = str(input('\nCONTINUE?\n"Y" or "N"\
                                \n\t--> ')).lower()
            if choice != 'y' or 'n':
                #
                choice = str(input('\nTry Again--Please enter "Y" or, \
                                    "N"\n\t--> ')).lower()
                                    
        # if user enters anything other than a string    
        except ValueError:
            #
            choice = str(input('\nThat was not a valid entry.\
                                Please enter "Y" or "Yes"; or, \
                                "N" or "No"\n\t--> ')).lower()
        else:
            # Quit the program
            if choice == 'n' or 'no':
                print('Goodbye.') 
        

def getString():
    # local variables
    threeWords = False
    
    # ask the user to enter a string
    aString = str(input('\nNEW WORD SET\n \
                          Enter a sentance below. \
                          (Please note that sentances must contain at least\
                          three words). \
                          \n\tEnter string here:\t--> ')).lower()
    
    while threeWords != False:
        if aString.find(" ") >= 3:
            threeWords = True
        else:
            aString = str(input('\nSENTENCE MUST CONTAIN AT LEAST THREE WORDS\
                                 \n\tEnter string here:\t--> ')).lower()
    
    # use split method to convert string into a separated list
    splitString = aString.split()
                                  
    return splitString

#
def pigLatin():
    ...

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