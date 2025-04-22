list = []


def main() :
    print("""
Welcome to Pakudex: Tracker Extraordinaire!
Enter max capacity of the Pakudex: 30
The Pakudex can hold 30 species of Pakuri. 

    """)

    keepRunning = True

    while keepRunning :
        print ("""
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
     
        """)


    userInput = input('What would you like to do?')

    if userInput == 1 :
        if (len(list) == 0):
            print("No Pakuri in Pakudex yet!")
        else :
            for index, pakuri in enumerate(list) :
                print(f"{index}. {pakuri}")

    elif userInput == 2:
        userInput = input("Enter the name of the species to display: ")
        print()

    #still building here, gonna work on pakuri first though


main()
#hello
