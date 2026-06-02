from dataclasses import dataclass

@dataclass
class Hex:
    biome: str = ""
    distance_to_ocean:int = None
    elevation: float = 0.0
    moisture: float = 0.0
    temperature: float = 0.0
