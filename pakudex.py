from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20):
        self.capacity: int = 20
        self.pakuri_list: list[Pakuri] = []

    def get_size(self) -> int:
        return len(self.pakuri_list)

    def get_capacity(self) -> int:
        return self.capacity

    def get_species_array(self) -> list[str] | None:
        if not self.pakuri_list:
            return None
        return [i.get_species() for i in self.pakuri_list]

    def get_stats(self, species: Pakuri) -> list[int] | None:
        if species in self.pakuri_list:
            return [species.attack, species.defense, species.speed]
        else:
            return None

    def sort_pakuri(self) -> None:
        self.pakuri_list.sort(key=lambda i: i.species)

    def add_pakuri(self, species: Pakuri) -> bool:
        if len(self.pakuri_list) == self.capacity:
            return False
        else:
            self.pakuri_list += [species]
            return True

    def evolve_species(self, species: Pakuri) -> bool:
        if species in self.pakuri_list:
            species.evolve()
            return True
        else:
            return False


def main():
    pass


if __name__ == "__main__":
    main()
