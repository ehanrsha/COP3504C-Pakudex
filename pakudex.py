from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20):
        self.capacity: int = capacity
        self.pakuri_list: list[Pakuri] = []

    def get_size(self) -> int:
        return len(self.pakuri_list)

    def get_capacity(self) -> int:
        return self.capacity

    def get_species_array(self) -> list[str] | None:
        if not self.pakuri_list:
            return None
        return [i.get_species() for i in self.pakuri_list]

    def get_stats(self, input: str) -> list[int] | None:
        x: Pakuri | None = next(
            (x for x in self.pakuri_list if x.species == input), None
        )
        if isinstance(x, Pakuri):
            return [x.attack, x.defense, x.speed]
        else:
            return None

    def sort_pakuri(self) -> None:
        self.pakuri_list = sorted(self.pakuri_list, key=lambda pakuri: pakuri.species)

    def add_pakuri(self, input: str) -> bool:
        to_add: Pakuri | None = next(
            (x for x in self.pakuri_list if x.species == input), None
        )
        if to_add is not None:
            return False
        else:
            self.pakuri_list += [Pakuri(input)]
            return True

    def evolve_species(self, input: str) -> bool:
        to_evolve: Pakuri | None = next(
            (x for x in self.pakuri_list if x.species == input), None
        )
        if isinstance(to_evolve, Pakuri):
            to_evolve.evolve()
            return True
        else:
            return False


def main():
    pass


if __name__ == "__main__":
    main()
