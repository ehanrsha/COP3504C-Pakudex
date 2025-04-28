class Pakuri:

    def __init__(self, species: str):
        self.attack: int = (len(species) * 7) + 9
        self.defense: int = (len(species) * 5) + 17
        self.speed: int = (len(species) * 6) + 13
        self.species: str = species

    def get_attack(self):
        return self.attack

    def get_species(self):
        return self.species

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack: int):
        self.attack = new_attack

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
