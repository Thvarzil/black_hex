from collections import deque

from hex import Hex
from hex_grid import HexGrid

def calculate_coastal_proximity(hex_grid:HexGrid):
    queue = deque()
    hexes = hex_grid.grid

    for (x,y),hex in hexes.items():
        # if ocean add to queue
        if hex.biome == "Ocean":
            queue.append((x,y))
        
        # while queue, check neighbors, if no dist, add dist and add to queue
    while queue:
        current = queue.popleft()
        neighbors = hex_grid.calc_neighbors(current[0],current[1])

        for neighbor in neighbors:
            if hexes[neighbor].distance_to_ocean is None:
                hexes[neighbor].distance_to_ocean = hexes[current].distance_to_ocean+1
                queue.append(neighbor)
