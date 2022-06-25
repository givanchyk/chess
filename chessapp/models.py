import datetime

from django.db import models
from django.utils import timezone

class Game(models.Model):
    fen = models.CharField(max_length=200)
    # white_player = models.CharField(max_length=200)
    # black_player = models.CharField(max_length=200)
# class Player(models.Model):
#     name = models.CharField(max_length=30)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)