# Fitness Club Diet Evaluation
# Daily carb and fat gram calculator

# Define global constants to use in Main() and showAll()

# Ask user to enter daily total of grams of carbs consumed +
# convert string to float for computation
dailyFatGrams = float(input('Enter the fat grams consumed: '))

# Ask user to enter daily total of grams of carbs consumed +
# convert string to float for computation
dailyCarbGrams = float(input('Enter the carbohydrate grams consumed: '))

# global name for computation of daily fat grams
fatCalories = dailyFatGrams * 9
# global name for computation of daily carb grams
carbCalories = dailyCarbGrams * 4

# Main = User's info + computation
def main():
    # Calculate fat calories
    fatCalories = dailyFatGrams * 9

    # Calculate carb calories
    carbCalories = dailyCarbGrams * 4

# Call function
main()

# ShowAll = results of computation from Main
def showAll():
    print('Grams of fat: ', dailyCarbGrams)
    print('Fat calories: ', fatCalories)
    print('Grams of carbs: ', dailyFatGrams)
    print('Carb calories: ', carbCalories)

# Call function
showAll()
