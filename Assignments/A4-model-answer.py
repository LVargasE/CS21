"""
Assignment 4
CS 21A
Instructor Solution
"""


# Named constants
INITIAL_BARS = 15;    # 15 items
DEFAULT_AMOUNT = 15;  # $15

def main():
    # Local variables
    letter = ''
    length = 0
    amount = 0

    available = 0
    amountDue = 0

    # initial values
    available = INITIAL_BARS;
    amountDue = DEFAULT_AMOUNT;

    # show initial data
    print ("Initial Account Settings:" + \
           "\n Available Bars:  ", available, \
           "\n Cost (so far) this month: $", amountDue, "\n")


    # Get menu choices from the user until s/he says "quit".
    while letter != 'Q' and letter != 'q':

        letter = input("Menu: " + \
              "\n  B (show Bill and starts new month)" + \
              "\n  A (show Available number of bars for the current month) " + \
              "\n  C (Consume bars now)" + \
              "\n  P (Purchase additional bars for current month)" + \
              "\n  Q (show bill and Quit) \n\n  Your Choice: ")

        # this letter is not one of the legal types
        while letter != 'B' and letter != 'b' and letter != 'A' and letter != 'a' \
              and letter != 'C' and letter != 'c' and letter != 'P' and letter != 'p' \
              and letter != 'Q' and letter != 'q':
            letter = input("Use B, A, C, P or Q, please.")

        if letter == 'B' or letter == 'b':
            # print bill ...
            print("Closing bill for month:" + \
                  "\n Unused Bars (lost):  ", available, \
                  "\n Final amount due immediately: $", amountDue, \
                  "\n\n Starting new month ...")

            # ... and begin a new month
            available = INITIAL_BARS
            amountDue = DEFAULT_AMOUNT



        # Nothing happens here except for showing the available bars which is
        # already done at the end of the loop.
        elif letter == 'A' or letter == 'a':
            print("")

        elif letter == 'C' or letter == 'c':
            # get number of bars to Consume
            amount = int(input("\n  Number of bars you want to Consume: "))

            while amount <= 0 or amount > 10:
                print("Sorry, amounts must be between 1 and 10. \n")
                amount = int(input("\n  Number of bars you want to Consume: "))

            if  amount > available:
                print("You exceeded your monthly allotment. " + \
                    "\n$15 / 10 bars added to current balances." )

                # add 10 bars and subtract number requested
                available += (10 - amount)
                amountDue += 15
            else:
                # normal operation - just subtracted number of bars consumed
                available -= amount


        elif letter == 'P' or letter == 'p':
            # add 10 more bars for $11
            amount = int(input("\n Purchase additional bars in " + \
                                         "sets of 10 (1-3): "))

            while amount < 1 or amount > 3:
                print("Request canceled.  Must be between 1 and 3.")
                amount = int(input("\n Purchase additional bars in " + \
                                         "sets of 10 (1-3): "))

            available += ( amount * 10)
            amountDue += (amount * 11)


        # test for quit
        elif letter == 'q' or letter == 'Q':
            print("Final bill: $", amountDue)
            print("\nThank you for using the Candy Locker")

        # in all cases, show bars available for current month
        print("Available bars: ", available, "\n")

    # Done with the loop and exiting
    print("\nGood bye.\n")

#call the main function
main()
   
