# screen
W, H                                = 1280, 720
FPS                                 = 60

# assets
ASSETS_PATH                         = 'assets_finaux'
ASSETS_SIZES                        = {
    
}
# dictionnaire pour l'instant non utilisé, pourrait servir plus tard à assigner une taille à chaque asset

# cartes
MAP_CSV_FILES_PATH                  = f'{ASSETS_PATH}/cartes'
MAP_GROUND_FILE_PATH                = f'{MAP_CSV_FILES_PATH}/monde_sol.csv'

# world loading
MINIMAP_SIZE_DIVIDER                = 5

# world rendering
TILE_SIZE                           = 64
ADDED_SAFETY_TILES                  = 1
# number of additional tiles rendered in each direction to avoid voids (when the player moves its camera)
# i don't even know why i made this variable, any value besides 1 will cause bugs and won't make any sense...

# minimap (currently, can also be considered part of 'world rendering')
MINIMAP_FORMATS                     = [(1, H/W), (1, 1), (1, 0.7)]
MINIMAP_CURRENT_FORMAT              = MINIMAP_FORMATS[2]
MINIMAP_DECALAGE                    = (10, 10) # en pixels
MINIMAP_CAMERA_INDICATOR_COLOR      = 'red'
MINIMAP_CAMERA_INDICATOR_WITDH      = 2 # en pixels
MINIMAP_CAMERA_INDICATOR_ADDED_SIZE = 2 # en tiles
# n'ajoute aucune tile, sert juste à rendre plus grand l'indicateur de caméra sur la minimap (ou plus petit)
MINIMAP_BORDER_COLOR                = 'black'
MINIMAP_BORDER_WIDTH                = 4 # en pixels
# optional setting to increase the size of the camera indicator

# camera
CAMERA_SPEED                        = 50 # en pixels
# plus TILE_SIZE sera élevée plus la vitesse sera lente (car l'offset maximum sera plus grand)