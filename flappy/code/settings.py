WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DT = 60  # frames per second

# first level
# TODO: Level generator
BLOCK_MAP = [
    "666666666666",
    "444444444444",
    "333333333333",
    "222222222222",
    "111111111111",
    "            ",
    "            ",
    "            ",
    "            ",
]
COLOR_LEGEND = {
    "1": "blue",
    "2": "green",
    "3": "red",
    "4": "orange",
    "5": "purple",
    "6": "bronze",
    "7": "gray",
}
"""
# TODO: draw block sprites in grayscale:
1. top
2. bottom
3. right
4. left
5. center
6. bottomleft
7. bottomright
8. topleft
9. topright
# TODO: find a way to convert grayscale to CMY in pygame for start
"""
GAP_SIZE = 2
BLOCK_HEIGHT = WINDOW_HEIGHT / len(BLOCK_MAP) - GAP_SIZE
BLOCK_WIDTH = WINDOW_WIDTH / len(BLOCK_MAP[0]) - GAP_SIZE
