#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Swamp Essence"
COST = 3
RARITY = 'C'
DESC = "Spawn a Lesser Leech Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Lesser Leech' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

