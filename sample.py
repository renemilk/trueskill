#!/usr/bin/env python

from __future__ import print_function
import trueskill,random

# The output of this program should match the output of the TrueSkill
# calculator at:
#
#   http://atom.research.microsoft.com/trueskill/rankcalculator.aspx
#
# (Select game mode "custom", create 4 players each on their own team,
# check the second "Draw?" box to indicate a tie for second place,
# then click "Recalculate Skill Level Distribution".  The mu and sigma
# values in the "after game" section should match what this program
# prints.

# The objects we pass to AdjustPlayers can be anything with skill and
# rank attributes.  We'll create a simple Player class that has
# nothing else.

class Player(object):
	def __init__(self,name):
		self.name = name

# Create four players.  Assign each of them the default skill.  The
# player ranking (their "level") is mu-3*sigma, so the default skill
# value corresponds to a level of 0.

alice = Player('alice')
alice.skill = (25.0, 25.0/3.0)

bob = Player('bob')
bob.skill = (25.0, 25.0/3.0)

chris = Player('chris')
chris.skill = (25.0, 25.0/3.0)

darren = Player('darren')
darren.skill = (25.0, 25.0/3.0)

players = [alice, bob, chris, darren]

# The four players play a game.  Alice wins, Bob and Chris tie for
# second, Darren comes in last.  The actual numerical values of the
# ranks don't matter, they could be (1, 2, 2, 4) or (1, 2, 2, 3) or
# (23, 45, 45, 67).  All that matters is that a smaller rank beats a
# larger one, and equal ranks indicate draws.
try:
	import sys
	iterations = int(sys.argv[1])
except:
	iterations = 1
	
random.seed()
with open('skills.csv','wb') as skilltable:
	skilltable.write('#iteration\t')
	for p in players:
		skilltable.write('%s_mu\t%s_sigma\t'%(p.name,p.name))
	skilltable.write('\n')
	
	for i in range(iterations):
		alice.rank = random.randint(0,4)
		bob.rank = random.randint(0,4)
		chris.rank = random.randint(0,4)
		darren.rank = random.randint(0,4)

		# Do the computation to find each player's new skill estimate.

		trueskill.AdjustPlayers(players)
		skilltable.write('%i\t'%i)
		for p in players:
			skilltable.write('%f\t%f\t'%p.skill)
		skilltable.write('\n')

# Print the results.

print(" Alice: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(alice.skill))
print("   Bob: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(bob.skill))
print(" Chris: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(chris.skill))
print("Darren: mu={0[0]:.3f}  sigma={0[1]:.3f}".format(darren.skill))
