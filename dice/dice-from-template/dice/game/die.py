import random


# TODO: Implement the Die class as follows...
# 1) Add the class declaration. Use the following class comment.
class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        side_to_points (dict): A translator between value and the number of points it is worth.
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __inti__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0
        self.side_to_points = {}
    
    def roll(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, 6)
        self.side_to_points = {
            '1': 100,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 50,
            '6': 0
        }
        #print(self.value)
        #print(self.__dict__)
        self.points = self.side_to_points[str(self.value)]