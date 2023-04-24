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