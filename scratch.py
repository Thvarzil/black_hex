hexgrid = [
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""]
    ]

# grid dimensions -1 due to 0 index
xmax = 4
ymax = 4

# pointy top hex grid, row 2 is to the right of row 1
# non-horizontal neighbors are (x-1+y%2,y+-1),(x+y%2,y+-1)
# if we pass coord 2,2 it should return [(1, 2), (1, 1), (1, 3), (3, 2), (2, 1), (2, 3)]
# if we pass coord 2,3 it should return [(1, 3), (2, 2), (2, 4), (3, 3), (3, 2), (3, 4)]
# TODO write tests
def calcNeighbors(x:int,y:int)->list[tuple[int,int]]:
    neighbors:list[tuple[int,int]] = []
    offset = y%2

    if x>0:
        neighbors.append((x-1,y))
        if y>0:
            neighbors.append((x-1+offset,y-1))
        if y<ymax:
            neighbors.append((x-1+offset,y+1))
    
    if x<xmax:
        neighbors.append((x+1,y))
        if y>0:
            neighbors.append((x+offset,y-1))
        if y<ymax:
            neighbors.append((x+offset,y+1))

    print(neighbors)
    return neighbors

# Hex generation order of operations
# Determine N/S Polarity
# Apply gradient temperature
# Apply elevation noise 
# - implied determination of ocean/water hexes
# Apply precipitation noise

