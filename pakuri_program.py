from pakuri import Pakuri
from pakudex import Pakudex


def main():
    print(
        """
Welcome to Pakudex: Tracker Extraordinaire!
Enter max capacity of the Pakudex: 30
The Pakudex can hold 30 species of Pakuri. 

    """
    )

    keepRunning = True
    pakudex = Pakudex()

    while keepRunning:
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

    userInput = input("What would you like to do?")
    try:
        userInput = int(userInput)

    except Exception:
        print("What would you like to do? Unrecogniezd menu selection!\n")
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
        case 3:
            userInput = input("Enter the name of the species to add: ")
        case 4:
            userInput = input("Enter the name of the species to evolve: ")
        case 5:
            userInput = input("Enter the name of the species to display: ")
        case 6:
            pakudex.sort_pakuri()
        case _:
            print("What would you like to do? Unrecognized menu selection!\n")
            pass


if __name__ == "__main__":
    main()
