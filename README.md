# shortest-path-to-block-algorithm
Algorithm choosing which block you should take. Based on preferences.

Example:
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
With this data provided, it will choose 3rd index (4th element). 
It has only school, but it has only one step to store, and one step to gym.
So based on this information it's the best block for you
