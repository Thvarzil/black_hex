whittaker_biomes = {
    "Tropical Rainforest": Polygon([(20, 400), (30, 400), (30, 200), (20, 130)]),
    "Tropical Seasonal Forest / Savanna": Polygon([(20, 130), (30, 200), (30, 100), (20, 40)]),  # removed self-intersecting (20,60),(24,40)
    "Subtropical Desert": Polygon([(20, 40), (30, 100), (30, 0), (20, 0)]),
    "Temperate Rain Forest": Polygon([(5, 300), (20, 400), (20, 130), (12, 100), (5, 100)]),
    "Temperate Seasonal Forest": Polygon([(5, 100), (12, 100), (20, 60), (20, 40), (5, 50)]),
    "Temperate Grassland / Desert": Polygon([(5, 50), (20, 40), (20, 0), (5, 0)]),
    "Boreal Forest / Taiga": Polygon([(-5, 100), (5, 100), (5, 50), (-15, 40)]),  # (-14,40) → (-15,40), removed redundant point
    "Tundra": Polygon([(-15, 40), (5, 50), (5, 25), (-5, 25)]),  # straightened upper boundary to match Boreal's lower edge
    "Alpine / Arctic Desert": Polygon([(-15, 0), (-15, 40), (-5, 25), (5, 25), (5, 0)])
}