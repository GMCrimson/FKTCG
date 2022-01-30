#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Own Medicine"
COST = 3
RARITY = 'C'
DESC = "Your opponent burns 2 cards. If he or she milled last turn, he or she burns 5 cards instead."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if enemy.milled == True:
		yield from enemy.burn(5)
	else:
		yield from enemy.burn(2)
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

