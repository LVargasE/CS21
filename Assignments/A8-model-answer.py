'''
Assignment 8
CS 21A
Instructor Solution
'''

# Named constants
MIN_WORDS = 3

def main():

    for i in range(1,4):

        print("\nNEW WORD SET")

        # Receive user input
        userWords = getString()

        print("\nWords made into Pig Latin:")
        print(pigLatin(userWords))

        print("\nWords made into Turkey Irish:")
        print(turkeyIrish(userWords))

        print("\n# of vowels in the words: ",countVowels(userWords))
        print("")
    # end for loop

#end main()


# Gets the string from the user and validates it.
#   Returns the list of words.
def getString():

    userString = input("Enter a string: ")

    # Divide the input into individual words
    words = userString.split()

    while len(words) < MIN_WORDS:
        print("The string must have at least 3 words in it.\n")
        userString = input("Enter a string: ")
        words = userString.split()

    return words
# end getString()


# Accepts the user's string and will convert it to Pig Latin by putting the first
#   letter at the end and adding 'ay'
#   returns the string to be displayed
def pigLatin(wordList):

    resultString = ""

    # Loop that changes each word
    for i in range(len(wordList)):

        item = wordList[i].lower()

        # For each word, change the order and add ending
        currentWord = item[1:] + item[0] + "ay"

        # Add adapted word to the result
        resultString += currentWord

        # If more words to be added, add a space to the result
        if i < len(wordList) + 1:
            resultString += " "

    return resultString

# end pigLatin


# turkeyIrish accepts the list of words and then will place 'ab' in front of
#   each vowel in each word
#   returns the string to be displayed
def turkeyIrish(wordList):

    resultString = ""
    i = 0

    # Loop that changes each word
    for word in wordList:

        word = word.lower() #wordList[i].lower()
        currentWord = ""

        # move through each letter in each word
        for letter in word:

            if letter in "aeiou":
                # add "ab" infron of each vowel
                currentWord += "ab" + letter
            else:
                # don't add anything
                currentWord += letter
        # end for loop

        # Add adapted word to the result
        resultString += currentWord

        # If more words to be added, add a space to the result
        if i < len(wordList) + 1:
            resultString += " "

        i += 1
    # end for loop

    return resultString

# end turkeyIrish


# countVowels accepts the list of words and then will count the number of vowels in all words
#  returns the number of vowels
def countVowels(wordList):

    total = 0

    # Loop that changes each word
    for i in range(len(wordList)):

        word = wordList[i].lower()

        # move through each letter in each word
        for letter in word:

            if letter in "aeiou":
                total += 1

        # end for loop
    # end for loop

    return total
# end countVowels



#call the main function
main()
