# Defining the list for recipes and ingredients
recipe_list = []
ingredients_list = []

# Take recipe takes the input form the user for the following variables
def take_recipe():
    name = input('Input name of the recipe: ')
    cooking_time = int(input('What is the cooking time(min): '))
    ingredients = input('What ingredients are in this recipe (separate by commas): ')

    # Assign these to recipe dictionary
    recipe = { 'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients }

    return recipe

# "n" How many recipes does the user want to enter?
n = int(input('How many recipes would you like to make? '))

# "n" a "for" will append the Recipe to the recipe list
for i in range(n):
    recipe = take_recipe()
    ingredients = recipe['ingredients'].split(',')
    for ingredient in ingredients:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipe_list.append(recipe)

# Setting the filter/sorting difficulty params
for recipe in recipe_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) <= 5:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 5:
        recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 5:
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 5:
        recipe['difficulty'] = 'Hard' 

    # Define what will be shown to the user
    print('==========================')
    print('recipe: ', recipe['name'])
    print('cooking_time(min): ', recipe['cooking_time'])
    print('ingredients: ', recipe['ingredients'])
    print('difficulty: ', recipe['difficulty'])

# Params for printing ingredients
# Define what will be shown to the user
def print_ingredients():
    ingredients_list.sort()
    print('==========================')
    print('All available ingredients for all recipes')
    print('*****************************************')

# Call the function to print each recipe
    for ingredient in ingredients_list:
        print(ingredient)

# Call the function to print ingredients
print_ingredients()
