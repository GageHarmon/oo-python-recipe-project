class Allergy:
    all_allergies = []
    
    def __init__ (self, user, ingredient):
        self.user = user
        self.ingredient = ingredient
        Allergy.all_allergies.append(self)
        
    @classmethod
    def all(cls):
        return cls.all_allergies