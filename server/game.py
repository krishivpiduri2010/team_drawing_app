"""
Contains the game class that saves the game data
"""


class Game:
    def __init__(self):
        self.data = []
        self._create_grid()

    def clear(self):
        self._create_grid()

    def _create_grid(self):
        self.data = [[(255, 255, 255) for _ in range(500)] for _ in range(500)]
