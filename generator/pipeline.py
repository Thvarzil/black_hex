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

from generator.elevation import generate_elevation
from generator.moisture import generate_moisture
from hex_grid import HexGrid

def run_generation(seed:int):
    hexgrid = HexGrid()
    
    generate_elevation(hexgrid, seed)
    generate_moisture(hexgrid, seed)

    hexgrid.print_grid()
