from classes.Game import Game

def main() -> None:
    game = Game()

    while True:

        status = game.getStatus()

        if status == "QUIT":
            game.gameQuit()
            break
        elif status == "START":
            pass
        elif status == "RESTART":
            game = Game()
            game.gameUpdate()
            continue

        game.gameUpdate()

if __name__ == "__main__":
    main()