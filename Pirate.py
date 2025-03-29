


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
            print("Invalid direction!")
            return False
        # Below code checks if the move that is initiated is a valid move or not.
        if island.valid_move(new_x, new_y):
            self.__x_coordinate, self.__y_coordinate = new_x, new_y
            self.__thirsty += 1
            return True
        # if not valid then this message is printed to the screen
        else:
            print("Cannot move there!")
            return False

    # a method to reset the thirst level to zero
    def drink_grog(self):
        self.__thirsty = 0
        print("Thirst quenched.")

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
