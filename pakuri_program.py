from pakuri import Pakuri
from pakudex import Pakudex


def main():
    capacity: int = int(
        input(
            " Welcome to Pakudex: Tracker Extraordinaire! Enter max capacity of the Pakudex: "
        )
    )
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    running = True
    pakudex = Pakudex(capacity)

    while running:
        print(
            """
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit"""
        )

        userInput = input("What would you like to do? ")
        try:
            userInput = int(userInput)

        except Exception:
            print("Unrecogniezd menu selection!\n")
            pass

        match userInput:
            case 1:
                if not pakudex.pakuri_list:
                    print("No Pakuri in Pakudex yet!")
                else:
                    for index, pakuri in enumerate(pakudex.pakuri_list):
                        print(f"{index}. {pakuri}")

            case 2:
                userInput = input("Enter the name of the species to display: ")

                dataList: list[int] | None = pakudex.get_stats(userInput)
                if dataList is None:
                    print("Error: No such Pakuri!")
                else:
                    print()
                    print(f"Species: {userInput}")
                    print(f"Attack: {dataList[0]}")
                    print(f"Defense: {dataList[1]}")
                    print(f"Speed: {dataList[2]}")

            case 3:
                userInput = input("Enter the name of the species to add: ")
                newPakuri = Pakuri(userInput)
                if newPakuri in pakudex.pakuri_list:
                    print("Error: Pakudex already contains this species!")
                elif len(pakudex.pakuri_list) == pakudex.capacity:
                    print("Error: Pakudex is full!")
                else:
                    print(
                        f"Pakuri species {newPakuri.get_species()} successfully added!"
                    )

            case 4:
                userInput = input("Enter the name of the species to evolve: ")
                if pakudex.evolve_species(Pakuri(userInput)):
                    print(f"{userInput} has evolved!")
                else:
                    print("Error: No such Pakuri!")

            case 5:
                userInput = input("Enter the name of the species to display: ")
                print("Pakuri have been sorted!")

            case 6:
                print("Thanks for using Pakudex! Bye!")
                running = False

            case _:
                print("What would you like to do? Unrecognized menu selection!\n")


if __name__ == "__main__":
    main()
