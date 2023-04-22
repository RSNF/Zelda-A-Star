import os

class AssetUtils:

    def getMap(mapName: str) -> list:
        if not mapName.endswith(".txt"):
            mapName = mapName + ".txt"

        file = open("src/assets/files/" + mapName, 'r')

        mapa = list()

        for line in file:
            mapaLine = list()
            for letter in line:
                if letter == '\n':
                    mapa.append(mapaLine)
                else:
                    mapaLine.append(letter)

        return mapa

    def getSprites() -> dict:
        pathSprites = "src/assets/sprites/"
        files = os.listdir(pathSprites)

        sprites = dict()

        for name in files:
            sprites[name.split('.')[0]] = pathSprites + name
        
        return sprites

    def getTextures() -> dict:
        pathTextures = "src/assets/textures/"
        files = os.listdir(pathTextures)

        textures = dict()

        for name in files:
            textures[name.split('.')[0]] = pathTextures + name
        
        return textures

if __name__ == "__main__":
    mapa = AssetUtils.getMap(input())
    sprites = AssetUtils.getSprites()
    textures = AssetUtils.getTextures()

    for linha in mapa:
        print(''.join(linha))

    print()
    
    for chave in sprites:
        print(chave + ' -> ' + sprites[chave])

    print()

    for chave in textures:
        print(chave + ' -> ' + textures[chave])