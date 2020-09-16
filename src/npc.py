import random
import tracery
from tracery.modifiers import base_english

import json
import re

# Names generated from Markov/Tracery:
# https://gist.github.com/JKirchartz/cd80079547e3ebdcf7ff34e8ed4103f9

rules = {
  'origin': '#hello.capitalize#, #location#!',
  'hello': ['hello', 'greetings', 'howdy', 'hey'],
  'location': ['world', 'solar system', 'galaxy', 'universe']
}

names = {
  'name': '#firstname.capitalize# #lastname.capitalize#',
  'firstname': ['Erik', 'Robb', 'Greg', 'Pat', 'Uriah', 'Loren'],
  'lastname': ['Dragonsworn', 'Placeholder', 'LastName', 'SomethingNeat']
}

name_grammar = tracery.Grammar(names)
name_grammar.add_modifiers(base_english)

class NPC(object):
  def __init__(self, _type, location):
    self._x = location[0]
    self._y = location[1]
    self._symbol = "\u04E6" #"&"
    self._type   = _type
    self._name   = name_grammar.flatten("#name#")

    self._msg_index = 0

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    self._msgs = []
    for i in range(6):
      self._msgs.append(grammar.flatten("#origin#"))
#    self._msgs = [\
#    'I have a long and drawn out story to tell, would you like to hear?',\
#    'I suppose I should\'ve put a Yes/No option in the last one huh.',\
#    'Oh well, perhaps next time.'\
#    ]
    # emotional state
    # PC affinity

  def getName(self):
    return self._name

  def getCurrentMessage(self):
    retval = self._msgs[self._msg_index]
    self._msg_index += 1
    if self._msg_index > len(self._msgs)-1:
      self._msg_index = 0

    return retval

  def getPos(self):
    return self._x, self._y

  def move(self):
    # 50% chance to move
    if random.random() > 0.3:
      moves = [[-1,0],[1,0],[0,1],[0,-1]]
      return random.choice(moves)
    return None

  def updatePosition(self, xdiff, ydiff):
    self._x += xdiff 
    self._y += ydiff
