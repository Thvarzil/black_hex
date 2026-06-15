from hex_grid import HexGrid
from generator.apply_biomes import apply_biomes


def make_grid(temperature, moisture):
    grid = HexGrid(seed=0, xsize=1, ysize=1)
    grid.grid[(0, 0)].temperature = temperature
    grid.grid[(0, 0)].moisture = moisture
    return grid


def test_tile_inside_biome_region_gets_biome_assigned():
    # temperature=25, moisture=300 falls inside "Tropical Rainforest"
    grid = make_grid(temperature=25, moisture=300)
    apply_biomes(grid)
    assert grid.grid[(0, 0)].biome == "Tropical Rainforest"


def test_tile_outside_all_biome_regions_keeps_empty_biome():
    grid = make_grid(temperature=-50, moisture=500)
    apply_biomes(grid)
    assert grid.grid[(0, 0)].biome == ""
