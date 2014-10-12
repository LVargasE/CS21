# Assignment 2
# Instructor Solution CS 21A

# Global constants for calories
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4

# main module
def main():

    # Get grams fat
    grams_fat = float(input("Enter the fat grams consumed: "))

    # Get grams carbs
    grams_carbs = float(input("Enter the carbohydrate grams consumed: "))

    # Calculate calories from fat
    calories_fat = grams_fat * CALORIES_FROM_FAT

    # Calculate calories from carbs
    calories_carbs = grams_carbs * CALORIES_FROM_CARBS

    # print calories and carbs
    show_all(grams_fat, grams_carbs, calories_fat, calories_carbs)


# The show_all function accepts the number of grams of fat and of carbs,
# as well as the calories from fat and from carbs, as arguments
# and displays the resulting calories
def show_all(grams_fat, grams_carbs, calories_fat, calories_carbs):
    print ("Grams of fat: ", grams_fat)
    print ("Fat calories: ", calories_fat)
    print ("Grams of carbs: ", grams_carbs)
    print ("Carb calories: ", calories_carbs)

# Call the main function
main()
