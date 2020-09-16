import random
import tracery
from tracery.modifiers import base_english

rules = {
  'origin': '#hello.capitalize#, #location#!',
  'hello': ['hello', 'greetings', 'howdy', 'hey'],
  'location': ['world', 'solar system', 'galaxy', 'universe']
}

names = {
  'name': '#firstname.capitalize# #lastname.capitalize#',
  'firstname': ['Anger', 'Sorrow', 'Puke', 'Fart', 'Madness', 'Unspeakable'],
  'lastname': ['Dragonsworn', 'Stinkface', 'Placeholder', 'Uggo', 'LastNameHA']
}

name_grammar = tracery.Grammar(names)
name_grammar.add_modifiers(base_english)

class Enemy(object):
  def __init__(self, _type, location):
    ## THIS CAN ALL BE ABSTRACTED ITNO A SUPER CLASS
    self._x = location[0]
    self._y = location[1]
    self._symbol = "!"#\u04E6" #"&"
    self._type   = _type
    self._name   = name_grammar.flatten("#name#")
    self._hp     = 100
    self._ac     = 2

    self._msg_index = 0

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    self._msgs = []
    for i in range(6):
      self._msgs.append(grammar.flatten("#origin#"))
    ###
