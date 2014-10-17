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

    # Get the regular price for all packages
    retailPrice = packageQuantity * RETAIL_PRICE

    # Get the discount amount
    discountAmount = computeDiscount(packageQuantity, retailPrice)

    # Calculate total amount
    totalAmount = retailPrice - discountAmount

    showPurchase(discountAmount, totalAmount, packageQuantity)

def getPackageQuantity():
    quantity = int(input("Enter the number of packages purchased: "))
    return quantity

def computeDiscount(packageQuantity, retailPrice):

    # conditional structure to determine discount amount
    if packageQuantity <= 9:
      discount = 0
    elif packageQuantity >= 10 and packageQuanity <= 19:
      discount = retailPrice * DISCOUNT_20
    elif packageQuantity >= 20 and packageQuantity <= 49:
      discount = retailPrice * DISCOUNT_30
    elif packageQuantity >= 50 and packageQuantity <= 99:
      discount = retailPrice * DISCOUNT_40
    else:
      discountAmount = retailPrice * DISCOUNT_50
    return discount

def showPurchase(discountAmount, totalAmount, packageQuantity):
    print("Enter the number of packages purchase: ", packageQuantity)
    print("Discount Amount: $", format(discountAmount, ',.2f'), sep='')
    print("Total Amount: $", format(totalAmount, ',.2f'), sep='')

# Call the main function
main()
