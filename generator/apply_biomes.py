from shapely import Polygon, Point, contains

from hex_grid import HexGrid

BIOMES = {
    "Tropical Rainforest": Polygon([(20, 400), (30, 400), (30, 200), (20, 130)]),
    "Savanna": Polygon([(20, 130), (30, 200), (30, 100), (20, 40)]), 
    "Subtropical Desert": Polygon([(20, 40), (30, 100), (30, 0), (20, 0)]),
    "Temperate Rainforest": Polygon([(5, 300), (20, 400), (20, 130), (12, 100), (5, 100)]),
    "Seasonal Forest": Polygon([(5, 100), (12, 100), (20, 60), (20, 40), (5, 50)]),
    "Grassland": Polygon([(5, 50), (20, 40), (20, 0), (5, 0)]),
    "Taiga": Polygon([(-5, 100), (5, 100), (5, 50), (-15, 40)]),  
    "Tundra": Polygon([(-15, 40), (5, 50), (5, 25), (-5, 25)]),  
    "Frigid Desert": Polygon([(-15, 0), (-15, 40), (-5, 25), (5, 25), (5, 0)])
}

def apply_biomes(hexgrid: HexGrid):
    hexes = hexgrid.grid
    for y in range(hexgrid.ysize):
        for x in range(hexgrid.xsize):
            biome_point = Point(hexes[(x,y)].temperature,hexes[(x,y)].moisture)

            for biome, area in BIOMES.items():
                if contains(area,biome_point):
                    hexes[(x,y)].biome = biome
                    break
