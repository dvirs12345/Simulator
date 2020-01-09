class Board:
    """
    This class represents a simulation board
    Attributes:
        x_size - The x size of the board. default is 1000
        y_size - The y size of the board. default is 1000
    """

    def __init__(self, x_size=1000, y_size=600, robots=[], foods=[]):
        self.x_size = x_size
        self.y_size = y_size
        self.robots = robots
        self.foods = foods
