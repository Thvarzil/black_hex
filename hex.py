from dataclasses import dataclass

@dataclass
class Hex:
    biome: str = ""
    distance_to_ocean:int = None
    elevation: float = 0.0
    elevation_m: int = 0 
    moisture: float = 0.0
    temperature: float = 0.0
    temperature_c: float = 0.0
