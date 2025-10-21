# Recipe Generator

# The user will input ingredients they have in their pantry and the program will output recipes that can be created with those ingredients
import json
import os

DATABASE_FILE = "recipes.json"

# Load recipes from the JSON file (or start empty if file doesn't exist)
def load_recipes():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    else:
        return {}  # Start with an empty dictionary

# Save recipes to the JSON file
def save_recipes(recipes):
    with open(DATABASE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

#----------------------------------- CORE GENERATOR FUNCTIONS --------------------------------------

#The first option will allow the user to find a recipe to cook using available ingredients they have inputed

#Define the function for finding a recipe using available ingredients
def function_find():
    recipes = load_recipes()

# If no recipes stored in the JSON file database, print an error messages instructing user to add some first
    if not recipes:
        print("\nNo recipes found, try adding some first!")
        return

# Ask the user to input the ingredients they have and convert the inputed string into lowercase to create uniformity with recipe database
    ingredients = input("\nWhat ingredients do you have?: ").lower()

#Split inputed ingredients into a list seperated at the comma
    list_ingredients = [item.strip() for item in ingredients.split(",")]

    available_recipes = []
    for recipe, required_ingredients in recipes.items():
        if all(item in list_ingredients for item in required_ingredients):
            available_recipes.append(recipe)

# Print the recipes that can be made, if they fall within the available recipes requirements
    if available_recipes:
        print("\nYou can make:")
        for recipe in available_recipes:
            print(f" - {recipe}")
    else:
        print("\nSorry, no matching recipes found with those ingredients.")

# If the user is missing ingredients, the code will generate a grocery list


#The user can add new recipes to the database

#Define the function to add a new recipe to the database as function_add
def function_add():
    recipes = load_recipes()
    recipe_name = input("\nEnter the name of the new recipe: ").strip()

    if recipe_name in recipes:
        print("That recipe already exists!")
        return

    ingredients = input("Enter the ingredients (separated by commas): ").lower()
    ingredient_list = [item.strip() for item in ingredients.split(",")]

    recipes[recipe_name] = ingredient_list
    save_recipes(recipes)
    print(f"\n✅ Recipe '{recipe_name}' added successfully!")

#The recipes in the database can be viewed and the ingredients in them will be listed

#Define the function to view an existing recipe in the database as function_view
def function_view():
    print("Recipe viewed.")


# The opening screen will ask the user what they want to do, based on a list of the defined options above

# Print each option on a new line in a numbered list
print("\nWelcome! What would you like to do today:")
print("1. Find something to cook!")
print("2. Add a new recipe to your database.")
print("3. View an existing recipe in the database.")
print("4. Exit")

# Ask the user to input their choice from the list above as a number from 1-4
option = input("Enter your choice (1-4): ")

# Use a conditional statement to perform the corresponding function defined above to the users inputed choice (i.e if they input 1, then perform function of option 1)
if option == "1":
    function_find()

elif option == "2":
    function_add()

elif option == "3":
    function_view()

elif option == "4":
    print("Exiting program.")


# If a number outside the list is entered, print an error message and ask the user to choose a correct number
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
