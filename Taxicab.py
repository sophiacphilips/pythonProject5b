# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 10/26/22
# This code finds total distance travelled when given a starting coordinate and a value of x and y to move.

class Taxicab:
    """
    represents a taxicab travelling on a 2D axis
    """
    def __init__(self, x, y):
        """
        creates new coordinates that cab will move to and sets odometer to 0
        """
        self._x=x
        self._y=y
        self._odometer= 0

    def get_coord_x(self):
        """
        gets new coord for x, for movement left or right
        """
        return self._x

    def get_coord_y(self):
        """
        returns distance moved up or down
        """
        return self._y

    def get_odometer(self):
         return self._odometer

    def move_x(self, distance):
        """
        distance moved left or right and odometer value
        """
        self._x += distance
        self._odometer += abs(distance) #use absolute value so answer provides total distance moved, not net distance

    def move_y(self, distance):
        """
        distance travelled up or down and odometer value
        """
        self._y += distance
        self._odometer += abs(distance)

cab=Taxicab(5,8) #creates a Taxicab object at coordinates (5, -8)
cab.move_x(3) # moves cab 3 units "right"
cab.move_y(-4) # moves cab 4 units "down"
cab.move_x(-1) #moves cab 1 unit "down"
print(cab.get_odometer()) #prints the current odometer reading