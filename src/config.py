# screen
W, H                                = 1280, 720
FPS                                 = 60

# assets
ASSETS_PATH                         = 'assets_finaux'

# cartes
MAP_CSV_FILES_PATH                  = f'{ASSETS_PATH}/cartes'
MAP_GROUND_FILE_PATH                = f'{MAP_CSV_FILES_PATH}/monde_sol.csv'

# world rendering
TILE_SIZE                           = 64
ADDED_SAFETY_TILES                  = 1
# number of additional tiles rendered in each direction to avoid voids (when the player moves its camera)
# i don't even know why i made this variable, any value besides 1 will cause bugs and won't make any sense...
MINIMAP_SIZE_DIVIDER                = 6
MINIMAP_PLAYER_SCALE                = 5
MINIMAP_PLAYER_COLOR                = 'red'

# camera
CAMERA_SPEED                        = 50