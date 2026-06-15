from hex_grid import HexGrid
from generator.coastal_prox import calculate_coastal_proximity


def make_grid(xsize, ysize):
    return HexGrid(seed=0, xsize=xsize, ysize=ysize)


def set_ocean(grid, x, y):
    grid.grid[(x, y)].biome = "Ocean"
    grid.grid[(x, y)].distance_to_ocean = 0


def test_no_ocean_tiles_leaves_all_distances_as_none():
    grid = make_grid(3, 1)
    calculate_coastal_proximity(grid)
    assert all(h.distance_to_ocean is None for h in grid.grid.values())


def test_land_adjacent_to_ocean_gets_distance_one():
    grid = make_grid(2, 1)
    set_ocean(grid, 0, 0)
    calculate_coastal_proximity(grid)
    assert grid.grid[(1, 0)].distance_to_ocean == 1


def test_distance_propagates_across_multiple_land_tiles():
    grid = make_grid(3, 1)
    set_ocean(grid, 0, 0)
    calculate_coastal_proximity(grid)
    assert grid.grid[(1, 0)].distance_to_ocean == 1
    assert grid.grid[(2, 0)].distance_to_ocean == 2


def test_ocean_tiles_already_visited_are_not_overwritten():
    # Two adjacent ocean tiles: when BFS processes tile A, tile B is already
    # distance=0 (not None), so it is skipped — neither gets bumped to 1.
    grid = make_grid(2, 1)
    set_ocean(grid, 0, 0)
    set_ocean(grid, 1, 0)
    calculate_coastal_proximity(grid)
    assert grid.grid[(0, 0)].distance_to_ocean == 0
    assert grid.grid[(1, 0)].distance_to_ocean == 0
