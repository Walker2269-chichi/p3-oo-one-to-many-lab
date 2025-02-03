# pet.py
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet instance to the 'all' class variable
        Pet.all.append(self)
        
        # If an owner is provided, associate the pet with the owner
        if owner:
            owner.add_pet(self)

    def __repr__(self):
        return f"{self.name} the {self.pet_type}"

# owner.py
class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("You can only add a Pet instance.")
        
        pet.owner = self  # Set the owner for the pet
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return self.name
