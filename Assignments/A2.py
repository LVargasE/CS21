# Fitness Club Diet Evaluation
# Daily carb and fat gram calculator

# Define global constants to use in Main() and showAll()

# global name for computation of daily fat grams
FAT_CALORIES = 9
# global name for computation of daily carb grams
CARB_CALORIES = 4

# Main = User's info + computation
def main():

    # Ask user to enter daily total of grams of carbs consumed +
    # convert string to float for computation
    dailyFatGrams = float(input('Enter the fat grams consumed: '))

    # Ask user to enter daily total of grams of carbs consumed +
    # convert string to float for computation
    dailyCarbGrams = float(input('Enter the carbohydrate grams consumed: '))

    # Calculate fat calories
    fatCalories = dailyFatGrams * FAT_CALORIES

    # Calculate carb calories
    carbCalories = dailyCarbGrams * CARB_CALORIES

    # Print calories and carbs
    showAll(dailyCarbGrams, fatCalories, dailyFatGrams, carbCalories)


# ShowAll = results of computation from Main
def showAll(dailyCarbGrams, fatCalories, dailyFatGrams, carbCalories):
    print('Grams of fat: ', dailyCarbGrams)
    print('Fat calories: ', fatCalories)
    print('Grams of carbs: ', dailyFatGrams)
    print('Carb calories: ', carbCalories)

# Call function
main()
