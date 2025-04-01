from poker.Card import Card
from poker.Hand import Hand
from poker.Setting import Setting
from poker.Player import Player
from poker.Deck import Deck
from poker.Poker import Poker

def time():
    Poker.timeStart = timer.time()

def track(msg=""):
    Poker.track(msg)

def getStrongestSetting(cards):
    player = Player(cards)
    return player.getStrongestSetting()

def getWeakestSetting(cards):
    player = Player(cards)
    return player.getWeakestSetting()
