# Assignment 3
# Software Sales Program

# Global constant for retail price of software
RETAIL_PRICE = 99
# Global constant for discounts to be used in computation
DISCOUNT_20 = .2
DISCOUNT_30 = .3
DISCOUNT_40 = .4
DISCOUNT_50 = .5

# Main Module
def main():

    # Get user to input the amount of packages
    packageQuantity = int(input("Enter the number of packages purchased: "))

    # conditional structure to determine discount amount
    if packageQuantity <= 9:
      discountAmount = 0
    elif packageQuantity >= 10 and packageQuanity <= 19:
      discountAmount = parckageQuantity * DISCOUNT_20
    elif packageQuantity >= 20 and packageQuantity <= 49:
      discountAmount = parckageQuantity * DISCOUNT_30
    elif packageQuantity >= 50 and packageQuantity <= 99:
      discountAmount = parckageQuantity * DISCOUNT_40
    else:
      discountAmount = parckageQuantity * DISCOUNT_50

    # Calculate total amount
    totalAmount = discountAmount - (packageQuantity * RETAIL_PRICE)

    showPurchase(discountAmount, totalAmount)

def showPurchase(discountAmount, totalAmount):
    print("Enter the number of packages purchase: ", packageQuantity)
    print("Discount Amount: ", discountAmount)
    print("Total Amount: $", totalAmount)

# Call the main function
main()
