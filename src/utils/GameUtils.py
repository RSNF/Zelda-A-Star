from classes.AStar import AStar

TILES = {
    "G": [ 10, "src/assets/textures/grass_tile0.png", None ],
    "D": [ 20, "src/assets/textures/desert_tile0.png", None ],
    "F": [ 100, "src/assets/textures/forest_tile0.png", "src/assets/sprites/grass0.png" ],
    "M": [ 150, "src/assets/textures/rocky_tile0.png", None ],
    "R": [ 180, "src/assets/textures/water_tile0.png", None ],
    "C": [ 10, "src/assets/textures/floor_tile0.png", None ],
    "B": [ 0, "src/assets/textures/wall_tile0.png", None ],
}

def get_tile_details(key:str) -> list:
    [cost, texture, sprite] = TILES[key]
    return [cost, texture, sprite]

def get_game_path(maps:list) -> list:
    pathHyrule = list()
    pathDungeon0 = list()
    pathDungeon1 = list()
    pathDungeon2 = list()

    mapHyrule = maps["hyrule"]
    mapDungeon0 = maps["dungeon0"]
    mapDungeon1 = maps["dungeon1"]
    mapDungeon2 = maps["dungeon2"]

    pathHyrule.extend(AStar.find_path(mapHyrule, mapHyrule.getStart(), mapHyrule.points[32][5])[1:])
    pathHyrule.extend(AStar.find_path(mapHyrule, mapHyrule.points[32][5], mapHyrule.points[17][39])[1:])
    pathHyrule.extend(AStar.find_path(mapHyrule, mapHyrule.points[17][39], mapHyrule.points[1][24])[1:])
    pathHyrule.extend(AStar.find_path(mapHyrule, mapHyrule.points[1][24], mapHyrule.points[5][6])[1:])
    pathHyrule.extend(AStar.find_path(mapHyrule, mapHyrule.points[5][6], mapHyrule.points[1][2])[1:])

    pathDungeon0.extend(AStar.find_path(mapDungeon0, mapDungeon0.getStart(), mapDungeon0.getEnd())[1:])
    pathDungeon0.extend(AStar.find_path(mapDungeon0, mapDungeon0.getEnd(), mapDungeon0.getStart())[1:])

    pathDungeon1.extend(AStar.find_path(mapDungeon1, mapDungeon1.getStart(), mapDungeon1.getEnd())[1:])
    pathDungeon1.extend(AStar.find_path(mapDungeon1, mapDungeon1.getEnd(), mapDungeon1.getStart())[1:])

    pathDungeon2.extend(AStar.find_path(mapDungeon2, mapDungeon2.getStart(), mapDungeon2.getEnd())[1:])
    pathDungeon2.extend(AStar.find_path(mapDungeon2, mapDungeon2.getEnd(), mapDungeon2.getStart())[1:])

    return {"hyrule": pathHyrule, "dungeon0": pathDungeon0, "dungeon1": pathDungeon1, "dungeon2": pathDungeon2}