from hex_grid import HexGrid
from generator.moisture import generate_moisture


def make_grid(xsize=3, ysize=3, distance_to_ocean=0):
    grid = HexGrid(seed=0, xsize=xsize, ysize=ysize)
    for hex in grid.grid.values():
        hex.distance_to_ocean = distance_to_ocean
    return grid


def test_moisture_is_set_on_every_tile():
    grid = make_grid()
    generate_moisture(grid, seed=0)
    assert all(isinstance(h.moisture, float) for h in grid.grid.values())


def test_tiles_closer_to_coast_get_higher_moisture():
    # coastal_bonus = max(0, 1 - distance/radius)^2, so distance=0 adds 1.0,
    # distance beyond radius adds 0 — same seed means same noise, so the
    # coastal tile will always have higher moisture
    grid_coastal = make_grid(xsize=1, ysize=1, distance_to_ocean=0)
    grid_inland = make_grid(xsize=1, ysize=1, distance_to_ocean=100)
    generate_moisture(grid_coastal, seed=0)
    generate_moisture(grid_inland, seed=0)
    assert grid_coastal.grid[(0, 0)].moisture > grid_inland.grid[(0, 0)].moisture
