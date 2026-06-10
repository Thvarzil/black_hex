import opensimplex
import math

from hex_grid import HexGrid

BASE_SCALE=0.04

def generate_temperature(hexgrid:HexGrid, seed:int, latitude:float,octaves=6, persistence=0.5, lacunarity=2.0):

    opensimplex.seed(seed)
    hexes = hexgrid.grid

    for y in range(hexgrid.ysize):
        for x in range(hexgrid.xsize):
            temperature = 0.0
            amplitude = 1.0
            frequency = 1.0
            max_value = 0.0

            for _ in range(octaves):
                temperature += opensimplex.noise2(
                    x=(x+0.5)* BASE_SCALE * frequency,
                    y=(y+0.5)* BASE_SCALE * frequency,
                    ) * amplitude
                max_value += amplitude
                amplitude *= persistence
                frequency *= lacunarity
            
            elevation_offset = -math.sqrt(max(hexes[(x,y)].elevation, 0)) * 30
            latitude_offset=((latitude*2)-1)*15
            temp_c = (temperature/max_value + 1) / 2 * 25
            hexes[(x,y)].temperature = int(temp_c + elevation_offset + latitude_offset)
