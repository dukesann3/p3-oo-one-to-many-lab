class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if not pet_type in Pet.PET_TYPES:
            raise TypeError("Pet type must be from the following: dog, cat, rodent, bird, reptile, exotic")
        self._pet_type = pet_type


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pets for pets in Pet.all if pets.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be a Pet object")
        pet.owner = self
    
    def get_sorted_pets(self):
        pets = self.pets()
        sorted_pets = sorted(pets, key=lambda pet: pet.name)
        return sorted_pets

