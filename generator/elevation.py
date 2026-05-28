import opensimplex

def generate_elevation(hexes, seed, octaves=6, persistence=0.5, lacunarity=2.0):
    opensimplex.seed(seed)
    
    for y, hex_row in enumerate(hexes):
        for x, hex in enumerate(hex_row):
            elevation = 0.0
            amplitude = 1.0
            frequency = 1.0
            max_value = 0.0

            for _ in range(octaves):
                elevation += opensimplex.noise2(
                    x=(x+0.5)*frequency,
                    y=(y+0.5)*frequency,
                    ) * amplitude
                max_value += amplitude
                amplitude *= persistence
                frequency *= lacunarity

            hex_row[x].elevation = elevation/max_value
