'''
File: PATVN002_assignment_1.py
Description: This module consists of a Treasure Island Game where 
the player is a Pirate who goes on a hunt for the treasure on an island 
and faces multiple water obstacles and the pirate is provided with a compass for guidance 
Author: Vraj Patel
ID: 110422159
Username: PATVN002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

# DISCLAIMER - Please do not provide a space after any inputs as it will be counted as an invalid input. Thank you :)

# importing random as library for its functnalities
import random


# Created a "Pirate" class to represent the player in the game and the user in real life
class Pirate:
    # constructor for initialization of attributes and all the attributes private
    def __init__(self, x_coordinate, y_coordinate):
        # x coordinate to show the position of pirate on x-axis
        self.__x_coordinate = x_coordinate
        # y coordinate to show the position of pirate on y-axis
        self.__y_coordinate = y_coordinate
        # thirst attribute to record the thirst level of the pirate and is given a default value of 0
        self.__thirsty = 0
        # this attribute represents the maximum thirst pirate has i.e. 5
        self.__max_thirsty = 5

    # defined a method "move" for the movement of pirate on the grid(island)
    def move(self, move_direction, island):
        # an if statement to check if the pirate is at max thirst or not
        if self.__thirsty >= self.__max_thirsty:
            print("Drink grog to move ")
            return False
        # if not at max thirst, the pirate moves to next tile and the below line of code records the new tile coordinate
        new_x, new_y = self.__x_coordinate, self.__y_coordinate
        # an if-elif-else statement for movement in all four directions on the island
        if move_direction == 'north':
            new_x -= 1
        elif move_direction == 'west':
            new_y -= 1
        elif move_direction == 'south':
            new_x += 1
        elif move_direction == 'east':
            new_y += 1
        else:
            print(
                "Invalid direction! Please enter any of these(north, south, east, west)")
            return False
        # Below code checks if the move that is initiated is a valid move or not.
        if island.valid_move(new_x, new_y):
            self.__x_coordinate, self.__y_coordinate = new_x, new_y
            self.__thirsty += 1
            return True
        # if not valid then this message is printed to the screen
        else:
            print("Its a water tile! Cannot move there!")
            return False

    # a method to reset the thirst level to zero
    def drink_grog(self):
        self.__thirsty = 0
        print("Thirst quenched. Lets keep on hunting")

    # a method to return the "x" and "y" coordinated of the treasure on the grid
    def check_treasure(self, treasure_x_coordinate, treasure_y_coordinate):
        return self.__x_coordinate == treasure_x_coordinate and self.__y_coordinate == treasure_y_coordinate

    # method to get the position of pirate of the grid
    def get_position(self):
        return self.__x_coordinate, self.__y_coordinate

    # getter method for the thirst level of the pirate on the grid
    def get_thirsty(self):
        return self.__thirsty

    # property to get the pirate position
    pirate_pos = property(get_position)
    # property to get the thirst level of the pirate
    pirate_thirst = property(get_thirsty)


# Created an "Island" class for displaying the grid
class Island:
    # constructor method for all the dimensions of the island
    def __init__(self, breadth, length, density):
        # this represents the breadth of island
        self.breadth = breadth
        # this represents the length of the island
        self.length = length
        # this represents the density of the water tiles on the grid according to their sizes
        self.density = density
        # a list that withholds the whole island
        self.grid = []
        # a function to create the whole grid
        self.create_grid()
        # a function to spawn the water tiles on the map
        self.put_water()

    # method to create the grid using a "while" loop
    def create_grid(self):
        # initializing the total tiles to be equal to the breadth og the grid times the length of the grid
        total_tiles = self.breadth * self.length
        # letting the created tiles on the screen to be 0
        created_tiles = 0
        # running a loop to check whether the created tiles is less than the total tiles
        while created_tiles < total_tiles:
            # appending an empty space everytimt a tile is created on the screen
            self.grid.append(' ')
            # incrementing the created tile by one
            created_tiles += 1

    # Method to check the move is valid or into a water tile
    def valid_move(self, x_axis, y_axis):
        # Checking if the "x" and "y" coordinates are within the grid limits or not
        if 0 <= x_axis < self.length and 0 <= y_axis < self.breadth:
            # initializing an index for display of the grid
            abc = x_axis * self.breadth + y_axis
            # Check whether the index moved is on a water tile or not.
            return self.grid[abc] != 'W'
        return False

    # method to spawn the water tiles on the grid
    def put_water(self):
        # Calculate the total number of water blocks to be placed based on island size and density
        water_blocks = int(self.breadth * self.length * self.density)
        # a loop to iterate over the water blocks and printing "W" where the index is met with the randomly generated tile
        for _ in range(water_blocks):
            iteration = random.randint(0, self.breadth * self.length - 1)
            self.grid[iteration] = 'W'

    # method to display the whole grid onto the screen
    def display(self, pirate_x_coordinate, pirate_y_coordinate, got_tres):
        """
        Nested while loop to display the whole island on the grid.
        horizontal distance refers to the length of the grid an vertical distance refer to the breadth of the island  

        If the horizontal distance is equal to the "x" coordinate and the vertical distance is equal to the 
        "y" coordinate of the pirate then marking the tile as "P"

        If the index in the grid representation equates to the index defined then marking the tile as "W".

        If no conditions are met then representing the tile as a land tile and putting a "•" there. 

        Incrementing the initial variables(indexes) to move over other tiles 
        """
        horizontal = 0
        while horizontal < self.length:
            vertical = 0
            while vertical < self.breadth:
                t = horizontal * self.breadth + vertical
                if (horizontal == pirate_x_coordinate) and (vertical == pirate_y_coordinate):
                    print(' P ', end=' ')
                elif self.grid[t] == 'W':
                    print(' W ', end=' ')
                else:
                    print(' • ', end=' ')
                vertical += 1
            print()
            horizontal += 1
        print()

# Created a "Treasure" class to spawn the treasure on the map


class Treasure:
    # constructor method to initiate the "x" and "y" coordinates of the treasure
    # All the attributes of this class are private i.e. they can only be accessed withi the class
    def __init__(self, treasure_x_coordinate, treasure_y_coordinate):
        # "x" coordinate of the treasure to show its position on x-axis
        self.__treasure_x_coordinate = treasure_x_coordinate
        # "y" coordiante of the treasure to show its position on y-axis
        self.__treasure_y_coordinate = treasure_y_coordinate

    # geetter method for the treasure coordinates initiated above
    def get_position(self):
        return self.__treasure_x_coordinate, self.__treasure_y_coordinate

    # property to get the treasure position
    treasure_pos = property(get_position)

# Created a "Compass" class for the navigation of player/pirate towards the treasure


class Compass:
    # method to get feedback on the screen regarding the distance of pirate from the treasure
    def give_feedback(self, pirate_x_coordinate, pirate_y_coordinate, treasure_x_coordinate, treasure_y_coordinate):
        """ 
        Initialized a variable to get the "x" axis and "y" axis position of the pirate on the grid 
        and the "x" axix and "y" axis position of treasure on the grid 

        All the axises of the treasure and pirate are given to a singular variable for calculation of 
        distance with ease
        """
        distance_from_treasure = self.__calculate_dist(
            pirate_x_coordinate, pirate_y_coordinate, treasure_x_coordinate, treasure_y_coordinate)

        # if-elif-else statements to give appropriate feedback based on the distance of pirate from the treasure
        if distance_from_treasure >= 7:
            print("You are cold. move closer to the treasure")
        elif 3 <= distance_from_treasure < 7:
            print("You are warmer")
        else:
            print("You are really hot, within reach of treasure")

    """ 
    Method below to calculate the distance based on the distance formula i.e. 
    √((x_2-x_1)²+(y_2-y_1)²) - referenced from google
    """

    def __calculate_dist(self, a1, b1, a2, b2):
        return ((a2 - a1) ** 2) ** 0.5 + ((b2 - b1) ** 2) ** 0.5


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
    #  Based on the difficulty the user chooses, the respective grid is spawned.
    choose_island_difficulty = {'Arrrd': (10, 10, 0.1), 'Arrrd..rrr': (
        20, 10, 0.2), 'Very Arrrrd': (30, 30, 0.35)}
    # Validation if the user enters invalid difficulty
    while True:
        input_true = input(
            "Choose : 'Arrrd', 'Arrrd..rrr', or 'Very Arrrrd': ")
        if input_true in choose_island_difficulty:
            break
        else:
            print(
                "Invalid difficulty. Please choose 'Arrrd', 'Arrrd..rrr', or 'Very Arrrrd'.")
        print()

    # The breadth, length and the density(water) is chosen according to the user input
    breadth, length, density = choose_island_difficulty[input_true]

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
        island.display(pirate_x, pirate_y, got_tres=False)
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
        elif action.startswith("move"):
            # Gets the direction of movement from the input the player made
            direction = action.split()[1]
            # if the pirate wants to move on the grid, the "move" method is called from the "Pirate" class
            if pirate.move(direction, island):
                # Checking if the pirate moved to a treasure tile then
                if pirate.check_treasure(treasure_x, treasure_y):
                    print("You found the treasure!")
                    break
        # If the player chooses "quit" as input
        if action == 'quit':
            print("Game over.")
            break
    else:
        print("Invalid action. Please choose again.")


