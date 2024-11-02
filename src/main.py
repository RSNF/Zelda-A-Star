from classes.Game import Game
from classes.Map import Map
from classes.Link import Link


def main() -> None:
    game = Game(672)
    mapHyrule = Map("hyrule", (27, 24), (7, 6), game.sizeWin)
    mapDungeon0 = Map("dungeon0", (26, 14), (3, 13), game.sizeWin)
    mapDungeon1 = Map("dungeon1", (25, 13), (2, 13), game.sizeWin)
    mapDungeon2 = Map("dungeon2", (25, 14), (19, 15), game.sizeWin)

    mapDict = {
        "hyrule": mapHyrule,
        "dungeon0": mapDungeon0,
        "dungeon1": mapDungeon1,
        "dungeon2": mapDungeon2,
    }

    link = Link(mapHyrule.points[27][24], 672 // len(mapHyrule.points))

    setattr(game, "map", mapHyrule)
    setattr(game, "maps", mapDict)
    setattr(game, "link", link)

    while True:

        status = game.getStatus()

        if status == "QUIT":
            game.gameQuit()
            break
        elif status == "START":
            game.gameStart()
        elif status == "RESTART":
            game = Game(672)
            link = Link(mapHyrule.points[27][24], 672 // len(mapHyrule.points))

            setattr(game, "map", mapHyrule)
            setattr(game, "maps", mapDict)
            setattr(game, "link", link)
            game.gameUpdate(0.05)
            continue

        game.gameUpdate(0)


if __name__ == "__main__":
    main()
