class Ingredient:
    
    all_ingredients = []

    def __init__(self, name, is_allergen=False):
        self.name = name
        self.is_allergen = is_allergen
        self.recipes = []
        self.allergies = []
        Ingredient.all_ingredients.append(self)

    @classmethod
    def all(cls):
        return cls.all
