from .recipe import Recipe
from .ingredient import Ingredient

class RecipeIngredient:
    all_instances = []

    def __init__(self, recipe, ingredient):
        self.recipe = recipe
        self.ingredient = ingredient
        RecipeIngredient.all_instances.append(self)

    @classmethod
    def all(cls):
        return cls.all_instances

    def get_ingredient(self):
        return self.ingredient

    def get_recipe(self):
        return self.recipe