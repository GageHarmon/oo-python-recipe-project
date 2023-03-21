from .user import User

class Recipe:
    all_recipes = []
    
    def __init__(self, name):
        self.name = name
        self. ingredients = []
        self.users = []
        Recipe.all_recipes.append(self)
        
    @classmethod
    def all(cls):
        return cls.all_recipes
    
    @classmethod
    def most_popular(cls):
        return max(cls.all_recipes, key=lambda recipe: len(recipe.users))
    
    def users(self):
        return self.users
    
    def ingredients(self):
        return self.ingredients
    
    def allergens(self):
        allergens = []
        for ingredient in self.ingredients:
            for user in User.all():
                if ingredient in user.allergens():
                    allergens.append(ingredient)
                    break
        return allergens
    
    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
            ingredient.recipes.append(self)