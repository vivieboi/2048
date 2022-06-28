#import sys, pygame
#pygame.init()
import tile
import random

class Board:
    def __init__(self):
        self.dimensions = "4x4"
        self.numTiles = 2
        #self.existing_tiles = []
        #self.available_positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        #self.taken_positions = []
        #self.starting_tile_numbers = [2,4]
        cant_merge_positions = []

    def merge(self, tile1, tile2):

        if tile1.position 
        if abs(tile1.position - tile2.position) == 1:
            if tile1.number == tile2.number:
                Tile.change_number(tile1)
                Tile.remove(tile2)

    def add_tile(self,tile):
        self.existing_tiles.append(tile)

        if tile.position < 5:
            if tile.position % 4 == 1:
                board_line1[0] = tile.number
            else if tile.position % 4 == 2:
                board_line1[1] = tile.number
            else if tile.position % 4 == 3:
                board_line1[2] = tile.number
            else:
                board_line1[3] = tile.number

        else if tile.position < 9:
            if tile.position % 4 == 1:
                board_line2[0] = tile.number
            else if tile.position % 4 == 2:
                board_line2[1] = tile.number
            else if tile.position % 4 == 3:
                board_line2[2] = tile.number
            else:
                board_line2[3] = tile.number
        
        else if tile.position < 13:
            if tile.position % 4 == 1:
                board_line3[0] = tile.number
            else if tile.position % 4 == 2:
                board_line3[1] = tile.number
            else if tile.position % 4 == 3:
                board_line3[2] = tile.number
            else:
                board_line3[3] = tile.number
        
        else:
            if tile.position % 4 == 1:
                board_line4[0] = tile.number
            else if tile.position % 4 == 2:
                board_line4[1] = tile.number
            else if tile.position % 4 == 3:
                board_line4[2] = tile.number
            else:
                board_line4[3] = tile.number
