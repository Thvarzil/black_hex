from hex_grid import HexGrid
from generator.elevation import generate_elevation


def make_grid(xsize=3, ysize=3):
    return HexGrid(seed=0, xsize=xsize, ysize=ysize)


def test_tiles_below_sea_level_become_ocean():
    # offset=-2.0 guarantees all noise values land below zero
    grid = make_grid()
    generate_elevation(grid, seed=0, offset=-2.0)
    for hex in grid.grid.values():
        assert hex.biome == "Ocean"
        assert hex.distance_to_ocean == 0
        assert hex.elevation_m == int(hex.elevation * 9_000)


def test_tiles_above_sea_level_are_not_classified():
    # offset=2.0 guarantees all noise values land above zero
    grid = make_grid()
    generate_elevation(grid, seed=0, offset=2.0)
    for hex in grid.grid.values():
        assert hex.biome == ""
        assert hex.distance_to_ocean is None
        assert hex.elevation_m == int(hex.elevation * 9_000)
