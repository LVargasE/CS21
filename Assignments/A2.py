# Fitness Club Diet Evaluation
# Daily carb and fat gram calculator

# Ask user to enter daily total of grams of fat consumed +
# convert string to float for computation
dailyFatGrams = float(input('Enter the fat grams consumed: '))

# Ask user to enter daily total of grams of carbs consumed +
# convert string to float for computation
dailyCarbGrams = float(input('Enter the carbohydrate grams consumed: '))

# Calculate fat calories
fatCalories = dailyFatGrams * 9

# Calculate carb calories
carbCalories = dailyCarbGrams * 4

# Display results of computation with function showAll
def showAll():
    print('Grams of fat: ', dailyCarbGrams)
    print('Fat calories: ', fatCalories)
    print('Grams of carbs: ', dailyFatGrams)
    print('Carb calories: ', carbCalories)

# Call function
showAll()
