from django.db import models
import json

____ = None


class Game(models.Model):
    # player constants, used in turn and mark
    PLAYER_NONE = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

    # turn choices
    # reference: https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices
    CURRENT_PLAYER_CHOICES = (
        (PLAYER_1, 'Player 1'),
        (PLAYER_2, 'Player 2'),
    )
    CURRENT_PLAYER_DICT = dict(CURRENT_PLAYER_CHOICES)
    current_player = models.IntegerField(choices=CURRENT_PLAYER_CHOICES, default=PLAYER_1)

    # used to determine draw
    turn_count = models.IntegerField(default=0)

    # status choices
    STATUS_UNFINISHED = 0
    STATUS_PLAYER_1_WIN = 1
    STATUS_PLAYER_2_WIN = 2
    STATUS_DRAW = 3
    STATUS_CHOICES = ____
    STATUS_DICT = ____
    status = ____

    # mark choices
    MARK_CHOICES = (
        (PLAYER_NONE, ' '),
        (PLAYER_1, 'O'),
        (PLAYER_2, 'X'),
    )
    MARK_DICT = ____

    # store mark info on boards as a 2-d list in json
    # e.g. [[0,0,1],[2,0,0],[0,0,0]]
    BOARD_SIZE = 3
    BOARD_EMPTY = []
    for _ in range(3):
        BOARD_EMPTY.append([____] * ____)
    BOARD_EMPTY = json.dumps(BOARD_EMPTY)
    board = models.CharField(max_length=32, default=BOARD_EMPTY)

    def __str__(self):
        return self.id
