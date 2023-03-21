from lib.allergy import *
from lib.ingredient import *
from lib.recipe import *
from lib.recipecard import *
from lib.recipeingredient import *
from lib.user import *

# code here

# Ingredients
sugar = Ingredient("Sugar")
flour = Ingredient("Flour")
butter = Ingredient("Butter")
chocolate = Ingredient("Chocolate")
salt = Ingredient("Salt")
pepper = Ingredient("Pepper")
peanuts = Ingredient("Peanuts")
milk = Ingredient("Milk")
eggs = Ingredient("Eggs")
water = Ingredient("Water")

# Recipes
chocolate_chip_cookies = Recipe("Chocolate Chip Cookies")
chocolate_chip_cookies.add_ingredients([sugar, flour, butter, chocolate, salt, eggs, water])
macarons = Recipe("Macarons")
macarons.add_ingredients([sugar, flour, eggs])
scrambled_eggs = Recipe("Scrambled Eggs")
scrambled_eggs.add_ingredients([eggs, milk, salt, pepper])

# Recipe Cards
rc1 = RecipeCard(user1, chocolate_chip_cookies, 5, "2022-01-01")
rc2 = RecipeCard(user2, macarons, 4, "2022-01-02")
rc3 = RecipeCard(user3, scrambled_eggs, 3, "2022-01-03")

# Users
john = User("John")
sara = User("Sara")

# Allergies
Allergy(john, peanuts)
Allergy(sara, eggs)

# Recipe Cards for Users
john.add_recipe_card(chocolate_chip_cookies, "2022-01-01", 5)
sara.add_recipe_card(chocolate_chip_cookies, "2022-01-02", 4)
john.add_recipe_card(macarons, "2022-01-03", 4)
sara.add_recipe_card(scrambled_eggs, "2022-01-04", 3)

# Printing recipe information
print("All recipes:")
for recipe in Recipe.all:
    print(recipe.name)
print()

print("Most popular recipe:", Recipe.most_popular().name)
print()

print("Users for Chocolate Chip Cookies:")
for user in chocolate_chip_cookies.users():
    print(user.name)
print()

print("Ingredients for Chocolate Chip Cookies:")
for ingredient in chocolate_chip_cookies.ingredients():
    print(ingredient.name)
print()

print("Allergens for Chocolate Chip Cookies:")
for ingredient in chocolate_chip_cookies.allergens():
    print(ingredient.name)
print()

print("All ingredients:")
for ingredient in Ingredient.all:
    print(ingredient.name)
print()

print("Most common allergen:", Ingredient.most_common_allergen().name)
print()

print("All recipe ingredients:")
for recipe_ingredient in RecipeIngredient.all:
    print("Recipe:", recipe_ingredient.recipe.name, "Ingredient:", recipe_ingredient.ingredient.name)
print()

print("All allergies:")
for allergy in Allergy.all:
    print("User:", allergy.user.name, "Ingredient:", allergy.ingredient.name)
print()

print("All users:")
for user in User.all:
    print(user.name)
print()

print("Recipes for John:")
for recipe in john.recipes():
    print(recipe.name)
print()

print("Allergies for John:")
for ingredient in john.allergens():
    print(ingredient.name)
print()

print("Top three recipes for John:")
for recipe in john.top_three_recipes():
    print(recipe.name)
print()

print("Most recent recipe for John:", john.most_recent_recipe().name)
print()


# do not remove 
# import ipdb; ipdb.set_trace()