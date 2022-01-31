#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Discarded Needles"
COST = 3
RARITY = 'C'
DESC = "Deal 2 damage to your opponent for each Drugged Node on the board."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	dmgToDeal = ply.nodes.count( 'Drugged' ) + enemy.nodes.count( 'Drugged' )
	await mechanics.damage( enemy, 2*dmgToDeal )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

