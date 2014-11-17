"""
Assignment 6
CS 21A
Instructor Solution
"""

# Needed for the remove and rename functions
import os

def main():
    # Local variables
    letter = ''
    name = 0
    score = 0
    result = False

    # display all of the records
    result = displayRecords()

    # let the user know if there was a problem
    if not result:
        print("There was a problem diplaying the data from the file.\n")


    # Get menu choices from the user until s/he says "quit".
    while letter != 'Q' and letter != 'q':

        letter = input("Menu: " + \
              "\n  C (make a Change to one of the records)" + \
              "\n  A (Add a record to the file) " + \
              "\n  R (Remove a record from the file)" + \
              "\n  D (Display the file with all records)" + \
              "\n  Q (time to Quit the program) \n\n  Your Choice: ")

        # this letter is not one of the legal types
        while letter not in ['C','c','A','a','R','r','D','d','Q','q']:
            letter = input("Use C, A, R, D or Q, please.")

        # make a Change to one of the records
        if letter == 'C' or letter == 'c':
            name  = input('Enter the name of the golfer you want to change the score for: ')
            score = int(input('Enter the new score: '))

            # Validate the score
            while score < 1 or score > 150:
                print("Request canceled.  The score must be between 1 and 150.")
                score = int(input("\n Enter the new score: "))


            # make a call to the function
            result = changeRecord(name, score)

            # let the user know the result
            if result:
                print("The change was successful and the file has been updated.\n")
            else:
                print("That golfer is not in the data file or there was an error.\n")

        # Add a record to the file
        elif letter == 'A' or letter == 'a':
            name  = input('Enter the name of the golfer you want to add to the file: ')

            # Validate the score
            while name == '':
                print("Request canceled.  The name must not be blank.")
                name  = input('Enter the name of the golfer you want to add to the file: ')


            score = int(input('Enter the score: '))

            # Validate the score
            while score < 1 or score > 150:
                print("Request canceled.  The score must be between 1 and 150.")
                score = int(input("\n Enter the new score: "))

            # make a call to the function
            result = addRecord(name, score)


            # let the user know the result
            if result:
                print("The addition was successful and the file has been updated.\n")
            else:
                print("There was a problem adding the golfer.\n")


        # Remove a record from the file
        elif letter == 'R' or letter == 'r':
            name  = input('Enter the name of the golfer you want to remove: ')

            # make a call to the function
            result = removeRecord(name)

            # let the user know the result
            if result:
                print("The removal was successful and the file has been updated.\n")
            else:
                print("That golfer is not in the data file.\n")

        # Display the file with all records
        elif letter == 'D' or letter == 'd':
            # make a call to the function
            result = displayRecords()

            # let the user know if there was a problem
            if not result:
               print("There was a problem diplaying the data from the file.\n")


        # test for quit
        elif letter == 'Q' or letter == 'q':

            print("\nThank you for using the Golf Scores program")



    # Done with the loop and exiting
    print("\nGood bye.\n")




# Displays all of the records in the data file.
def displayRecords():

    # Create a bool variable to use as a flag.
    found = False

    print("\nHere is the list of golfers in the data file:")

    try:
        # Open the file in append mode.
        golfer_file = open('golfers.txt', 'r')

        # Read the first record's name field.
        storedName = golfer_file.readline()

        # Read the rest of the file.
        while storedName != '':

            # Read the score field.
            storedScore = int(golfer_file.readline())

            # Strip the \n from the name.
            storedName = storedName.rstrip('\n')

            # Display the record.
            print('Name of Golfer: ', storedName)
            print('Score: ', storedScore)

            # Read the next name.
            storedName = golfer_file.readline()

        # get an extra line of space after the list
        print('')

        # Close the file.
        golfer_file.close()

        # Everything worked
        return True

    except IOError:
        # an error occurred
        return False





# Accepts the name to be searched for and the replacement score
# returns a true boolean for success and false for no name OR file error.
def changeRecord(searchName, score):

    # Create a bool variable to use as a flag.
    found = False

    try:
        # Open the file in append mode.
        golfer_file = open('golfers.txt', 'r')

        # Open the temporary file.
        temp_file = open('temp.txt', 'w')

        # Read the first record's name field.
        storedName = golfer_file.readline()

        # Read the rest of the file.
        while storedName != '':
            # Read the score field.
            storedScore = int(golfer_file.readline())

            # Strip the \n from the name.
            storedName = storedName.rstrip('\n')

            # Determine whether this record matches
            # the search value.
            if storedName == searchName:
                # Write the modified record to the temp file.
                temp_file.write(storedName + '\n')
                temp_file.write(str(score) + '\n')

                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(storedName + '\n')
                temp_file.write(str(storedScore) + '\n')

            # Read the next description.
            storedName = golfer_file.readline()


        # Close the golfer file and the temporary file.
        golfer_file.close()
        temp_file.close()

        # Delete the original golfers.txt file.
        os.remove('golfers.txt')

        # Rename the temporary file.
        os.rename('temp.txt', 'golfers.txt')

        # If the search value was found, all is good, if not found in the file, return false.
        if found:
            return True
        else:
            return False

    except IOError:
        # an error occurred
        return False




# Accepts the name and score for the record to be added.
# returns a boolean for success
def addRecord(name, score):

    try:
        # Open the file in append mode.
        golfer_file = open('golfers.txt', 'a')

        # Append the data to the file.
        golfer_file.write(name + '\n')
        golfer_file.write(str(score) + '\n')


        # Close the file.
        golfer_file.close()

        # everything went smoothly
        return True

    except IOError:
        # an error occurred
        return False



# Accepts the name of the record to be removed
# returns a true boolean for success and false for no name match OR file error.
def removeRecord(searchName):

    # Create a bool variable to use as a flag.
    found = False

    try:
        # Open the file in append mode.
        golfer_file = open('golfers.txt', 'r')

        # Open the temporary file.
        temp_file = open('temp.txt', 'w')

        # Read the first record's name field.
        storedName = golfer_file.readline()

        # Read the rest of the file.
        while storedName != '':
            # Read the score field.
            storedScore = int(golfer_file.readline())

            # Strip the \n from the name.
            storedName = storedName.rstrip('\n')

            # Determine whether this record matches
            # the search value.
            if storedName == searchName:
                # Write nothing to the temp file if found.

                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(storedName + '\n')
                temp_file.write(str(storedScore) + '\n')

            # Read the next name.
            storedName = golfer_file.readline()


        # Close the golfer file and the temporary file.
        golfer_file.close()
        temp_file.close()

        # Delete the original golfers.txt file.
        os.remove('golfers.txt')

        # Rename the temporary file.
        os.rename('temp.txt', 'golfers.txt')

        # If the search value was found, all is good, if not found in the file, return false.
        if found:
            return True
        else:
            return False

    except IOError:
        # an error occurred
        return False



#call the main function
main()
   
