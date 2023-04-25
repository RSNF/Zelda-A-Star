import utils.GameUtils as gu

from .Point import Point
from utils.AssetUtils import AssetUtils

class Map:
    
    def __init__(self, name:str, start:tuple, end:tuple, winSize:int) -> None:
        self.name = name
        self.start = start
        self.end = end
        self.winSize = winSize
        self.points = list()

        self.makeMap()

    def makeMap(self) -> None:
        mapa = AssetUtils.getMap(self.name)
        mapSize = len(mapa)
        gridFit = self.winSize // mapSize
        
        for i in range(mapSize):
            temp = list()
            for j in range(mapSize):
                (cost, texture, sprite) = gu.get_tile_details(mapa[i][j])

                if not sprite:
                    sprite = self.getAnySprite(i, j)

                point = Point(i, j, gridFit, mapSize, cost, texture, sprite, mapa[i][j])
                temp.append(point)
            self.points.append(temp)
        
        for linha in self.points:
            for point in linha:
                point.updateNeighbors(self.points)

    def getAnySprite(self, row, col) -> str:
        sprites = AssetUtils.getSprites()
        sprite = None

        if self.name == "hyrule":
            if (row == 32 and col == 5) or (row == 17 and col == 39) or (row == 1 and col == 24):
                sprite = sprites["dungeon_hole0"]
            elif row == 5 and col == 6:
                sprite = sprites["sword_guard0"]
            elif row == 1 and col == 2:
                sprite = sprites["master_sword0"]
        elif self.name == "dungeon0":
            if row == 3 and col == 13:
                sprite = sprites["chest0"]
            elif row == 26 and col == 14:
                sprite = sprites["dungeon_hole0"]
        elif self.name == "dungeon1":
            if row == 25 and col == 13:
                sprite = sprites["dungeon_hole0"]
            elif row == 2 and col == 13:
                sprite = sprites["chest0"]
        elif self.name == "dungeon2":
            if row == 25 and col == 14:
                sprite = sprites["dungeon_hole0"]
            elif row == 19 and col == 15:
                sprite = sprites["chest0"]

        return sprite

    def getStart(self) -> Point:
        (x, y) = self.start
        return self.points[x][y]
    
    def getEnd(self) -> Point:
        (x, y) = self.end
        return self.points[x][y]