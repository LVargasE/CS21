# Assignment 3
# CS 21A
# Instructor Solution


# Named constants
RETAIL_PRICE = 99

# main function
def main():
    # Local variables
    quantity = 0
    fullPrice = 0.0
    discountRate = 0.0
    discountAmount = 0.0
    totalAmount = 0.0

    # Get number
    quantity = int(input("Enter the number of packages purchased: "))

    # Calculate the discount rate
    if quantity > 99:
        discountRate = 50/100
    elif quantity > 49:
        discountRate = 40/100
    elif quantity > 19:
        discountRate = 30/100
    elif quantity > 9:
        discountRate = 20/100
    else:
        discountRate = 0


    # Calculate the full price
    fullPrice = quantity * RETAIL_PRICE

    # Calculate the discount amount
    discountAmount = fullPrice * discountRate

    #Calculate the total amount
    totalAmount = fullPrice - discountAmount

    # print results
    showPurchase(discountAmount, totalAmount)



# The showPurchase function accepts discountAmount, totalAmount as
# arguments and displays the amounts
def showPurchase(discountAmount, totalAmount):
    print ("Discount Amount: $", format(discountAmount, '.2f'))
    print ("Total Amount: $", format(totalAmount, '.2f'))

# Run the main function
main()
