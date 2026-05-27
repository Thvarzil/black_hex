import opensimplex

#TODO add fractal octaves
def generate_elevation(hexes, seed):
    # Highest elevation in Europe 5642m
    # Lowest elevation in Europe 
    opensimplex.seed(seed)
    
    for y, hex_row in enumerate(hexes):
        for x, hex in enumerate(hex_row):
            hex_row[x].elevation = opensimplex.noise2(x=x+0.5, y=y+0.5)

    print(hexes)
