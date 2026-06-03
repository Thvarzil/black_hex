from dataclasses import dataclass, field
from hex import Hex

@dataclass
class HexGrid:
    xsize: int = 50
    ysize: int = 50
    grid: dict[tuple[int,int],Hex] = field(default_factory=dict)

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
                hex = self.grid[(x,y)]
                biome_marker = ""
                if hex.elevation < 0:
                    biome_marker +="."
                elif hex.elevation < .25:
                    biome_marker +="="
                elif hex.elevation <.5:
                    biome_marker +="#"
                elif hex.elevation <.75:
                    biome_marker +="M"
                else:
                    biome_marker +="@"

                biome_marker += " "
                row += biome_marker
            
            print(row)

    def print_dto_grid(self):
        for y in range(self.ysize):
            # initialize the row, with rightward indent for odd rows
            row = ""
            if y%2==1:
                row+=" "

            for x in range(self.xsize):
                dto_marker = str(self.grid[(x,y)].distance_to_ocean)
                dto_marker += " "
                row += dto_marker

            print(row)
    
    def calc_neighbors(self,x:int,y:int)->list[tuple[int,int]]:
        neighbors:list[tuple[int,int]] = []
        offset = y%2

        if x>0:
            neighbors.append((x-1,y))
            if y>0:
                neighbors.append((x-1+offset,y-1))
            if y<self.ysize-1:
                neighbors.append((x-1+offset,y+1))
    
        if x<self.xsize-1:
            neighbors.append((x+1,y))
            if y>0:
                neighbors.append((x+offset,y-1))
            if y<self.ysize-1:
                neighbors.append((x+offset,y+1))

        return neighbors