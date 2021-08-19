"""
Holds the player class that stores data related to the participant
"""
from constants import *


class Player:
    def __init__(self, username):
        self.username = username
        self.selected_color = WHITE
