from dataclasses import dataclass

@dataclass
class Hex:
    elevation: float = 0.0
    temperature: float = 0.0
    humidity: float = 0.0
    biome: str = ""
