from classes.Game import Game
from classes.Map import Map
from classes.Link import Link

def main() -> None:
    game = Game(672)
    mapHyrule = Map("hyrule", (27, 24), (7, 6), game.sizeWin)
    mapDungeon0 = Map("dungeon0", (26, 14), (10, 3), game.sizeWin)
    mapDungeon1 = Map("dungeon1", (25, 13), (2, 13), game.sizeWin)
    mapDungeon2 = Map("dungeon2", (25, 14), (19, 15), game.sizeWin)

    # link = Link(mapHyrule.points[27][24], 672 // len(mapHyrule.points))
    link = Link.make_start(mapHyrule.points[27][24], 672 // len(mapHyrule.points))
    lista = list()
    setattr(game, 'map', mapHyrule)
    setattr(game, 'link', link)

    while True:

        status = game.getStatus()

        if status == "QUIT":
            game.gameQuit()
            break
        elif status == "START":
            game.gameStart()
        elif status == "RESTART":
            game = Game(672)
            link = Link.make_start(mapHyrule.points[27][24])
            # link = Link(mapHyrule.points[27][24], 672 // len(mapHyrule.points))
            setattr(game, 'map', mapHyrule)
            setattr(game, 'link', link)
            game.gameUpdate(0)
            continue
        
        game.gameUpdate(1)

if __name__ == "__main__":
    main()