from dataclasses import dataclass
from hex import Hex

@dataclass
class HexGrid:
    xsize: int = 5
    ysize: int = 5
    grid: dict[tuple[int,int],Hex]

    def __post_init__(self):
        for x in range(self.xsize):
            for y in range(self.ysize):
                self.grid[(x,y)]=Hex()

    def print_grid(self):
        for y in range(self.ysize):
            # initialize the row, with rightward indent for odd rows
            row = ""
            if y%2==1:
                row+=" "
            
            for x in range(self.xsize):
                # Cast biome to letter or x for undefined
                biome_marker = self.grid[(x,y)].biome[0] if self.grid[(x,y)].biome else "x"
                biome_marker += " "
                row += biome_marker
            
            print(row)