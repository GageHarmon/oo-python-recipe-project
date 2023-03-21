from .allergy import Allergy
from .recipecard import RecipeCard

class User:
    all_users = []
    
    def __init__(self, name):
        self.name = name
        self.allergies = []
        self.recipe_cards = []
        User.all_users.append(self)
        
    @classmethod
    def all(cls):
        return cls.all_users
    
    def recipes(self):
        recipes = []
        for recipe_card in self.recipe_cards:
            recipes.append(recipe_card.recipe)
        return recipes
    
    def add_recipe_card(self, recipe, date, rating):
        recipe_card = RecipeCard(self, recipe, date, rating)
        self.recipe_cards.append(recipe_card)
        recipe.users.append(self)

    def declare_allergy(self, ingredient):
        allergy = Allergy(self, ingredient)
        self.allergies.append(allergy)
        ingredient.allergies.append(allergy)

    def allergens(self):
        allergens = []
        for allergy in self.allergies:
            allergens.append(allergy.ingredient)
        return allergens

    def top_three_recipes(self):
        sorted_recipe_cards = sorted(self.recipe_cards, key=lambda recipe_card: recipe_card.rating, reverse=True)
        top_three_recipe_cards = sorted_recipe_cards[:3]
        top_three_recipes = []
        for recipe_card in top_three_recipe_cards:
            top_three_recipes.append(recipe_card.recipe)
        return top_three_recipes

    def most_recent_recipe(self):
        sorted_recipe_cards = sorted(self.recipe_cards, key=lambda recipe_card: recipe_card.date, reverse=True)
        return sorted_recipe_cards[0].recipe                  
        