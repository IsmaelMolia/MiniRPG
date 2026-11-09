# screen
W, H                                = 1280, 720
FPS                                 = 60

# assets
ASSETS_PATH                         = 'assets_finaux'
ASSETS_SIZES                        = {
    
}

# cartes
MAP_CSV_FILES_PATH                  = f'{ASSETS_PATH}/cartes'
MAP_GROUND_FILE_PATH                = f'{MAP_CSV_FILES_PATH}/monde_sol.csv'

# world loading
MINIMAP_SIZE_DIVIDER                = 6
MINIMAP_TILES_LOADING_SIZE          = 8
# a lower value will reduce lag but decrease minimap detail (can even make cropped tiles, thus making black lines across the minimap)
# a higher value will increase lag but improve minimap detail (i don't think that it's noticeable above 8)
# i recommend 8

# world rendering
TILE_SIZE                           = 64
ADDED_SAFETY_TILES                  = 1
# number of additional tiles rendered in each direction to avoid voids (when the player moves its camera)
# i don't even know why i made this variable, any value besides 1 will cause bugs and won't make any sense...

# minimap (currently, can also be considered part of 'world rendering')
MINIMAP_PLAYER_SCALE                = 5
MINIMAP_PLAYER_COLOR                = 'red'
MINIMAP_CAMERA_INDICATOR_WITDH      = 1

# camera
CAMERA_SPEED                        = 50