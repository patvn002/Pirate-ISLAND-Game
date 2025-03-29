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