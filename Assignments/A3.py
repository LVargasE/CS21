# Assignment 3
# Software Sales Program

# Global constant for retail price of software
RETAIL_PRICE = 99
# Global constant for discounts to be used in percentage computation
DISCOUNT_20 = 0.20
DISCOUNT_30 = 0.30
DISCOUNT_40 = 0.40
DISCOUNT_50 = 0.50

# Main Module
def main():

    # Get the package quantity
    packageQuantity = getPackageQuantity()

    # Display/print number of packages
    print("Enter the number of packages purchase: ", packageQuantity)

    # Get the regular retail price for all packages
    retailPrice = packageQuantity * RETAIL_PRICE

    # Get the discount amount
    discountAmount = computeDiscount(packageQuantity, retailPrice)

    # Calculate total amount
    totalAmount = retailPrice - discountAmount

    # Show the discounted amount and the total amount!
    showPurchase(discountAmount, totalAmount)

# Using the return statement to use user's package number in other functions
def getPackageQuantity():
    quantity = int(input("Enter the number of packages purchased: "))
    return quantity

# Using the return statement and a boolean function to compute the right
# discount based on user's number. I couldn't use the logical operator
# without the boolean function's 'x' and 'y' to model the computation
def computeDiscount(x, y):

    # conditional structure to determine discount amount
    if x <= 9:
      discount = 0
    elif x >= 10 and x <= 19:
      discount = y * DISCOUNT_20
    elif x >= 20 and x <= 49:
      discount = y * DISCOUNT_30
    elif x >= 50 and x <= 99:
      discount = y * DISCOUNT_40
    else:
      discount = y * DISCOUNT_50
    return discount

# Shows the total discounted amount and total amount from main() with decimal
# places and commas
def showPurchase(discountAmount, totalAmount):
    print("Discount Amount: $", format(discountAmount, ',.2f'), sep='')
    print("Total Amount: $", format(totalAmount, ',.2f'), sep='')

# Call the main function
main()
