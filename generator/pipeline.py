"""
This file will need to:
 - Generate a random seed
 - Append layer names and encrypt to make 3 separate keys for each layer
 - Call each step of the generation process:
    1. Run elevation noise pass → `elevation` float per hex in -1..1 DONE
    2. Classify ocean: Apply variable elevation offset, hexes with positive elevation are above water DONE
    3. Compute `coast_proximity` per hex (BFS distance to nearest ocean tile, normalized)
    4. Run moisture noise pass; apply coast bonus scaled by `coast_proximity` and `base_humidity`
    5. Run temperature pass (latitude bias + elevation modifier + noise)
    6. Classify inland lakes
    7. Remaining non-water hexes → Whittaker biome lookup(temperature, moisture)
 - Return 2d list of hexes
"""
import xxhash

from secrets import randbelow

from generator.coastal_prox import calculate_coastal_proximity
from generator.elevation import generate_elevation
from generator.moisture import generate_moisture
from generator.temperature import generate_temperature
from hex_grid import HexGrid

def run_generation(seed:int=None):
    hexgrid = HexGrid()
    
    # we are assuming that we either got a usable seed or no input if we got to this point
    if not seed:
        seed = randbelow(2**32)

    generate_elevation(hexgrid, layer_seed(seed, "elevation"))
    calculate_coastal_proximity(hexgrid)
    generate_moisture(hexgrid, layer_seed(seed, "moisture"))
    generate_temperature(hexgrid, layer_seed(seed, "temperature"))

    print(f'Worldseed: {seed}')
    hexgrid.print_elevation_grid()

def layer_seed(base_seed:int, layer:str)->int:
    return xxhash.xxh32(f"{base_seed}:{layer}").intdigest()
    