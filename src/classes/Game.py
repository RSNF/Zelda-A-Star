import pygame
import time
import utils.GameUtils as gu

from classes.Point import Point

class Game:

    def __init__(self, sizeWin) -> None:
        self.sizeWin = sizeWin
        self.canvas = pygame.display.set_mode((sizeWin, sizeWin))
        self.canSwordSFX = True
        self.costs = {}
        self.total_cost = int(0)

        pygame.display.set_caption("Zelda A Star")
        pygame.init()
        pygame.mixer.init()

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
        if sleepTime != 0:
            time.sleep(sleepTime)
        self.conditionals()
        self.drawPoints()
        self.drawObjects()
        self.drawLink()
        self.drawGrid()
        pygame.display.update()

    def gameQuit(self) -> None:
        pygame.quit()
    
    def gameStart(self) -> None:
        if not hasattr(self, 'paths'):
            self.paths = gu.get_game_path(self.maps)
            self.path = self.paths["hyrule"]
            pygame.mixer.music.load("src/assets/music/hyrule.mp3")
            pygame.mixer.music.play()
            
            for key, points in self.paths.items():
                path_cost = sum(list(map(lambda point: point.cost, points)))
                self.costs[key] = ("Custo {} --> {}".format(key, path_cost))
                self.total_cost += path_cost


    def drawPoints(self) -> None:

        for linha in self.map.points:
            for point in linha:
                self.drawPoint(point)

    def drawPoint(self, point:Point) -> None:
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

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
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

        setattr(self.link, 'gridFit', gridFit)
        
        if hasattr(self, 'path') and len(self.path) != 0:
            self.link.moveLink(self.path.pop(0))

            (x, y) = self.link.point.getLocation()
            print("{} --> x = {}, y = {} : cost: {}".format(self.map.name, x, y, self.link.point.cost))

            if((x == 1 and y == 2) and self.map.name == "hyrule"):
                print("\n################ Custos ################")
                for key in self.costs:
                    print(self.costs[key])
                print("Custo total --> {}".format(self.total_cost))
        
        self.canvas.blit(self.link.sprite, (self.link.point.x, self.link.point.y))

    def drawGrid(self) -> None:
        mapSize = len(self.map.points)
        gridFit = self.sizeWin // mapSize

        for i in range(mapSize):
            pygame.draw.line(self.canvas, (0, 0, 0), (0, i * gridFit), (self.sizeWin, i * gridFit))
            for j in range(mapSize):
                pygame.draw.line(self.canvas, (0, 0, 0), (j * gridFit, 0), (j * gridFit, self.sizeWin))

    def conditionals(self) -> None:
        self.sfxConditionals(self.link.point.getLocation())

        if hasattr(self, 'path') and self.map.name == "hyrule":
            self.paths[self.map.name] = self.path

            if self.link.point.row == 32 and self.link.point.col == 5:
                self.map = self.maps["dungeon0"]
                self.path = self.paths["dungeon0"]
                self.musicConditionals()
            elif self.link.point.row == 17 and self.link.point.col == 39:
                self.map = self.maps["dungeon1"]
                self.path = self.paths["dungeon1"]
                self.musicConditionals()
            elif self.link.point.row == 1 and self.link.point.col == 24:
                self.map = self.maps["dungeon2"]
                self.path = self.paths["dungeon2"]
                self.musicConditionals()
        else:
            if hasattr(self, 'path') and len(self.path) == 0:
                self.map = self.maps["hyrule"]
                self.path = self.paths["hyrule"]
                self.musicConditionals()
        
    def musicConditionals(self) -> None:
        if self.map.name != "hyrule":
            pygame.mixer.music.load("src/assets/music/dungeon.mp3")
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.load("src/assets/music/hyrule.mp3")
            pygame.mixer.music.play(0)

    def sfxConditionals(self, pos:list) -> None:
        (row, col) = pos

        if self.map.name == "hyrule":
            if (row == 32 and col == 5) or (row == 17 and col == 39) or (row == 1 and col == 24):
                sound = pygame.mixer.Sound("src/assets/sfx/down_dungeon.wav")
                pygame.mixer.Sound.play(sound)
            elif row == 5 and col == 6:
                sound = pygame.mixer.Sound("src/assets/sfx/passed_guard.wav")
                pygame.mixer.Sound.play(sound)
                time.sleep(2)
            elif row == 1 and col == 2 and self.canSwordSFX:
                channel = pygame.mixer.Channel(1)
                sound = pygame.mixer.Sound("src/assets/sfx/get_sword.wav")
                channel.play(sound)
                self.canSwordSFX = not self.canSwordSFX
        else:
            if self.map.name == "dungeon0":
                if row == 3 and col == 13:
                    sound = pygame.mixer.Sound("src/assets/sfx/get_item.wav")
                    pygame.mixer.Sound.play(sound)
                    self.link.changeSprite(0, 0, True)
                    pygame.display.update()
                    time.sleep(2)
                elif row == 26 and col == 14:
                    sound = pygame.mixer.Sound("src/assets/sfx/down_dungeon.wav")
                    pygame.mixer.Sound.play(sound)
            elif self.map.name == "dungeon1":
                if row == 25 and col == 13:
                    sound = pygame.mixer.Sound("src/assets/sfx/down_dungeon.wav")
                    pygame.mixer.Sound.play(sound)
                elif row == 2 and col == 13:
                    sound = pygame.mixer.Sound("src/assets/sfx/get_item.wav")
                    pygame.mixer.Sound.play(sound)
                    self.link.changeSprite(0, 0, True)
                    pygame.display.update()
                    time.sleep(2)
            elif self.map.name == "dungeon2":
                if row == 25 and col == 14:
                    sound = pygame.mixer.Sound("src/assets/sfx/down_dungeon.wav")
                    pygame.mixer.Sound.play(sound)
                elif row == 19 and col == 15:
                    sound = pygame.mixer.Sound("src/assets/sfx/get_item.wav")
                    pygame.mixer.Sound.play(sound)
                    self.link.changeSprite(0, 0, True)
                    pygame.display.update()
                    time.sleep(2)