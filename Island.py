import random

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
    def display(self, pirate_x_coordinate, pirate_y_coordinate, treasure_found):
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