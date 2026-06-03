import opensimplex


from hex_grid import HexGrid

def generate_moisture(
        hexgrid:HexGrid, 
        seed, 
        base_humidity           =0.0,
        coast_influence_radius  =20,
        lacunarity              =2.0, 
        octaves                 =6, 
        persistence             =0.5, 
        ):
    opensimplex.seed(seed)
    hexes = hexgrid.grid
    


    for y in range(hexgrid.ysize):
        for x in range(hexgrid.xsize):
            moisture = 0.0
            amplitude = 1.0
            frequency = 1.0
            max_value = 0.0

            coastal_bonus = max(0, 1 - hexes[(x,y)].distance_to_ocean / coast_influence_radius) ** 2

            for _ in range(octaves):
                moisture += opensimplex.noise2(
                    x=(x+0.5)*frequency,
                    y=(y+0.5)*frequency,
                    ) * amplitude
                max_value += amplitude
                amplitude *= persistence
                frequency *= lacunarity

            hexes[(x,y)].moisture = moisture/max_value + base_humidity + coastal_bonus
