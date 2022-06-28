
class Tile:
    def __init__(self, number, position):
        self.number = number # number is assigned with game line of code initializing tile
        self.position = position

    def change_number(self):
        self.number *= 2

    def remove(self):
        del(self) # fix later on
