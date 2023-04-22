import pygame

class Game:

    def __init__(self) -> None:
        self.canvas = pygame.display.set_mode((672, 672))

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

    def gameUpdate(self) -> None:
        pygame.display.update()

    def gameQuit(self) -> None:
        pygame.quit()
    
    def gameStart(self) -> None:
        pass