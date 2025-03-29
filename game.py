from Island import Island
from Pirate import Pirate
from Compass import Compass
from Treasure import Treasure

import random


"""
This is the main game function i.e. outside all the classes defined above.

This function utilizes all the methods defined above and helps to spawn the grid 
with appropriate tile measurments and with required density of water and land and at last the treasure. 

This function helps to help the pirate move onto the grid in any preffered direction while checking 
every move and utilizing the "Compass" class to calculate the distance from the treasure and give feedback 
based on the distance on the screen. 

This function also helps the pirate to drink grog if thursty and quit the game at any stage. 
"""


def Game():
    print("Welcome to Treasure Island!")
    print("----------------------------")

    """
    The user is prompted to input the difficulty from the available options at the start of the game
    // Arrrd- Easy, Arrrd..rrr - Medium ,Very Arrrrd - Hard
    """
    choose_input = input("Choose : 'Arrrd', 'Arrrd..rrr', or 'Very Arrrrd': ")
    print()
    #  based on the difficulty the user chooses, the respective grid is spawned.
    choose_island_difficulty = {'Arrrd': (10, 10, 0.1), 'Arrrd..rrr': (
        20, 10, 0.2), 'Very Arrrrd': (30, 30, 0.35)}

    # The breadth, length and the density(water) is chosen according to the user input
    breadth, length, density = choose_island_difficulty[choose_input]

    # This variable calls the Island class from above
    island = Island(breadth, length, density)
    """
    This below lines of code is used to calculate the starting point of pirate on the grid and 
    dividing the length and breadth by 2 ensured the pirate spawns in the center of the grid
    """
    pirate_start_x = length // 2
    pirate_start_y = breadth // 2
    """
    A variable is assigned to get the start position of pirate on the island and called the 
    pirate class to get its fuctionalities
    """
    pirate = Pirate(pirate_start_x, pirate_start_y)
    # This below line of code is used to spawn the treasure on the map on random "x" and "y" coordinates
    treasure_x_coordinate = random.randint(0, length-1)
    treasure_y_coordinate = random.randint(0, breadth-1)
    """
    The below line of code creates an instance of the "Treasure" class using the randomly generated 
    coordinates of the treasure
    """
    treasure = Treasure(treasure_x_coordinate, treasure_y_coordinate)
    # Created an instance for compass class to use its methods
    compass = Compass()

    # Setting the initial condition to be True and running the game within a While loop
    run_game = True
    while run_game:
        # checks if the pirate is able to move by checking if at max thurst level
        if pirate.get_thirsty() == pirate._Pirate__max_thirsty:
            print("Drink grog to move!")

        # Storing the current position of the pirate on the island
        pirate_x, pirate_y = pirate.pirate_pos
        # Calling the display method from "Island" class to get the position of pirate and the status of treasure found
        island.display(pirate_x, pirate_y, treasure_found=False)
        # Storing the current position of treasure o the island
        treasure_x, treasure_y = treasure.get_position()
        # This provides the feedback based on the distance of player from the treasure
        compass.give_feedback(pirate_x, pirate_y, treasure_x, treasure_y)
        print()
        action = input(
            "Choose an action: 'move' (direction), 'drink grog', 'quit': ").lower()
        if action == 'drink grog':
            # drink_grog method is called from "Pirate" class
            pirate.drink_grog()
        # if the player inputs to move in the "action" prompt above
        elif action.startswith("move"):
            # Gets the direction of movement from the input the player made
            direction = action.split()[1]
            # if the pirate wants to move on the grid, the "move" method is called from the "Pirate" class
            if pirate.move(direction, island):
                # Checking if the pirate moved to a treasure tile then
                if pirate.check_treasure(treasure_x, treasure_y):
                    # Prints to the screen
                    print("You found the treasure!")
                    break
        # If the player chooses "quit" as input
        if action == 'quit':
            print("Game over.")
            # Breaks the loop and stops the game
            break
        # if the input is invalid then the player is asked to input the action again
    else:
        print("Invalid action. Please choose again.")


# This below line code calls the main game loop
Game()
