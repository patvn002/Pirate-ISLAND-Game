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
            print("You are cold")
        elif 3 <= distance_from_treasure < 7:
            print("You are warm")
        else:
            print("You are hot")

    """ 
    Method below to calculate the distance based on the distance formula i.e. 
    √((x_2-x_1)²+(y_2-y_1)²) - referenced from google
    """

    def __calculate_dist(self, a1, b1, a2, b2):
        return ((a2 - a1) ** 2) ** 0.5 + ((b2 - b1) ** 2) ** 0.5
