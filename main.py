#import sys, pygame
#pygame.init()

#screen = pygame.display.set_mode(320,240)

#ball = pygame.image.load("ball_test.jpg")

import random
import tile
import Board

#board = Board()
existing_tiles = []
available_positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
taken_positions = []
starting_tile_numbers = [2,4]

board_line1 = [0,0,0,0]
board_line2 = [0,0,0,0]
board_line3 = [0,0,0,0]
board_line4 = [0,0,0,0]

#creating first tile
position = available_positions.pop(random.choice(available_positions))
taken_positions.append(position)
number = random.choice(starting_tile_numbers)
tile1 = tile.Tile(number,position)

if tile1.position < 5:
    if tile1.position % 4 == 1:
        board_line1[0] = tile1.number
    else if tile1.position % 4 == 2:
        board_line1[1] = tile1.number
    else if tile1.position % 4 == 3:
        board_line1[2] = tile1.number
    else:
        board_line1[3] = tile1.number

else if tile1.position < 9:
    if tile1.position % 4 == 1:
        board_line2[0] = tile1.number
    else if tile1.position % 4 == 2:
        board_line2[1] = tile1.number
    else if tile1.position % 4 == 3:
        board_line2[2] = tile1.number
    else:
        board_line2[3] = tile1.number




#creating second tile
position = available_positions.pop(random.choice(available_positions))
taken_positions.append(position)
number = random.choice(starting_tile_numbers)
tile2 = tile.Tile(number,position)
print(tile2.position)
print(tile2.number)
print(available_positions)
print(taken_positions)
