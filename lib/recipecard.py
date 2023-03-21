class RecipeCard:
    
    all_recipe_cards = []

    def __init__(self, user, recipe, rating, date):
        self.user = user
        self.recipe = recipe
        self.rating = rating
        self.date = date
        RecipeCard.all_recipe_cards.append(self)

    @classmethod
    def all(cls):
        return cls.all_recipe_cards

    def user(self):
        return self.user

    def recipe(self):
        return self.recipe

    def date(self):
        return self.date

    def rating(self):
        return self.rating