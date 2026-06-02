import opensimplex

from hex_grid import HexGrid

BASE_SCALE=0.08

def generate_elevation(hexgrid:HexGrid, seed, octaves=6, persistence=0.5, lacunarity=2.0, offset=0.1):

    opensimplex.seed(seed)
    hexes = hexgrid.grid

    for y in range(hexgrid.ysize):
        for x in range(hexgrid.xsize):
            elevation = 0.0
            amplitude = 1.0
            frequency = 1.0
            max_value = 0.0

            for _ in range(octaves):
                elevation += opensimplex.noise2(
                    x=(x+0.5)* BASE_SCALE * frequency,
                    y=(y+0.5)* BASE_SCALE * frequency,
                    ) * amplitude
                max_value += amplitude
                amplitude *= persistence
                frequency *= lacunarity

            hexes[(x,y)].elevation = elevation/max_value + offset
            if hexes[(x,y)].elevation < 0:
                hexes[(x,y)].biome = "Ocean"
                hexes[(x,y)].distance_to_ocean = 0
