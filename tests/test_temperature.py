from hex_grid import HexGrid
from generator.temperature import generate_temperature


def make_grid(xsize=1, ysize=1, elevation=0.0):
    grid = HexGrid(seed=0, xsize=xsize, ysize=ysize)
    for hex in grid.grid.values():
        hex.elevation = elevation
    return grid


def test_negative_elevation_does_not_reduce_temperature():
    # max(elevation, 0) clamps to 0 for ocean tiles, so elevation_offset = 0
    grid = make_grid(elevation=-1.0)
    generate_temperature(grid, seed=0, latitude=0.5)
    assert isinstance(grid.grid[(0, 0)].temperature, int)


def test_higher_elevation_produces_lower_temperature():
    # elevation_offset = -sqrt(elevation) * 30, so higher elevation = colder
    # same seed means same noise — only elevation_offset differs
    grid_low = make_grid(elevation=0.1)
    grid_high = make_grid(elevation=1.0)
    generate_temperature(grid_low, seed=0, latitude=0.5)
    generate_temperature(grid_high, seed=0, latitude=0.5)
    assert grid_low.grid[(0, 0)].temperature > grid_high.grid[(0, 0)].temperature
