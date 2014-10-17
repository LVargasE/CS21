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

    # Display # of packages
    print("Enter the number of packages purchase: ", packageQuantity)

    # Get the regular price for all packages
    retailPrice = packageQuantity * RETAIL_PRICE

    # Get the discount amount
    discountAmount = computeDiscount(packageQuantity, retailPrice)

    # Calculate total amount
    totalAmount = retailPrice - discountAmount

    showPurchase(discountAmount, totalAmount)

def getPackageQuantity():
    quantity = int(input("Enter the number of packages purchased: "))
    return quantity

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

def showPurchase(discountAmount, totalAmount):
    print("Discount Amount: $", format(discountAmount, ',.2f'), sep='')
    print("Total Amount: $", format(totalAmount, ',.2f'), sep='')

# Call the main function
main()
