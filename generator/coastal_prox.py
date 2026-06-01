from collections import deque

from hex import Hex
from hex_grid import HexGrid

def calculate_coastal_proximity(hexes:HexGrid):
    queue = deque()
    for y, hex_row in hexes:
        for x, hex in hex_row:
            if 
