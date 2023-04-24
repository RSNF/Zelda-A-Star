import pygame
from classes.Point import Point

class Link:

    def __init__(self, point:Point, gridFit:int) -> None:
        self.point = point
        self.gridFit = gridFit
        self.sprite = pygame.image.load('src/assets/sprites/link0.png')
        self.sprite = pygame.transform.scale(self.sprite, (gridFit, gridFit))

    def changeSprite(self, x:int, y:int) -> None:
        sprite = ""

        if x != self.point.x:
            if x > self.point.x:
                sprite = 'src/assets/sprites/link4.png'
            else:
                sprite = 'src/assets/sprites/link2.png'
        elif y != self.point.y:
            if y < self.point.y:
                sprite = 'src/assets/sprites/link1.png'
            else:
                sprite = 'src/assets/sprites/link0.png'
            
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (self.gridFit, self.gridFit))
            

    def moveLink(self, point:Point) -> None:
        self.changeSprite(point.x, point.y)
        self.point = point