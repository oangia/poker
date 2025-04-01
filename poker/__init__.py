from poker.Core.Card import Card
from poker.Core.Hand import Hand
from poker.Core.Setting import Setting
from poker.Player import Player
from poker.Deck import Deck
from poker.Poker import Poker

def time():
    Poker.timer()

def track(msg=""):
    Poker.track(msg)

def getStrongestSetting(cards):
    player = Player(cards)
    return player.getStrongestSetting()

def getWeakestSetting(cards):
    player = Player(cards)
    return player.getWeakestSetting()
