class Point:
    
    def __init__(self, row:int, col:int, size:int, rows:int, cost:int, texture:str, sprite:str, terrain:str) -> None:
        self.row = row
        self.col = col
        self.x = col * size
        self.y = row * size
        self.rows = rows
        self.cost = cost
        self.texture = texture
        self.terrain = terrain
        self.neighbors = []

        if sprite:
            self.sprite = sprite

    def getLocation(self) -> list:
        return [self.row, self.col]
    
    def isBarrier(self) -> bool:
        return self.cost == 0
    
    def updateNeighbors(self, grid:list) -> None:
        self.neighbors = []

        if self.row < self.rows - 1 and not grid[self.row + 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.rows - 1 and not grid[self.row][self.col + 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col - 1])