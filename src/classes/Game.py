import pygame
import time

class Game:

    def __init__(self, sizeWin) -> None:
        self.sizeWin = sizeWin
        self.canvas = pygame.display.set_mode((sizeWin, sizeWin))

        pygame.display.set_caption("Zelda A Star")
        pygame.init()

    def getStatus(self) -> str:
        events = pygame.event.get()
        status: str = None

        for event in events:
            if event.type == pygame.QUIT:
                status = "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = "START"
                if event.key == pygame.K_r:
                    status = "RESTART"

        return status

    def gameUpdate(self, sleepTime:float) -> None:
        time.sleep(sleepTime)
        self.drawPoints()
        self.drawObjects()
        self.drawLink()
        self.drawGrid()
        pygame.display.update()

    def gameQuit(self) -> None:
        pygame.quit()
    
    def gameStart(self) -> None:
        pass

    def drawPoints(self) -> None:
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

        for linha in self.map.points:
            for point in linha:
                texture = pygame.image.load(point.texture)
                texture = pygame.transform.scale(texture, (gridFit, gridFit))
                self.canvas.blit(texture, (point.x, point.y))

    def drawObjects(self) -> None:
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

        for linha in self.map.points:
            for point in linha:
                if hasattr(point, "sprite"):
                    sprite = pygame.image.load(point.sprite)
                    sprite = pygame.transform.scale(sprite, (gridFit, gridFit))
                    self.canvas.blit(sprite, (point.x, point.y))

    def drawLink(self) -> None:
        self.canvas.blit(self.link.sprite, (self.link.point.x, self.link.point.y))

    def drawGrid(self) -> None:
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

        for i in range(mapSize):
            pygame.draw.line(self.canvas, (0, 0, 0), (0, i * gridFit), (self.sizeWin, i * gridFit))
            for j in range(mapSize):
                pygame.draw.line(self.canvas, (0, 0, 0), (j * gridFit, 0), (j * gridFit, self.sizeWin))