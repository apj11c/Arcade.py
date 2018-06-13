''' roulette.py
	
	Roulette Table Setup
	--------------------

	[From en.wikipedia.org/wiki/Roulette#Roulette_wheel_number_sequence]

	The pockets of the roulette wheel are numbered from 0 to 36.

	In number ranges from 1 to 10 and 19 to 28, odd numbers are red
	and even are black.
	In ranges from 11 to 18 and 29 to 36, odd numbers are black
	and even are red.

	There is a green pocket numbered 0 (zero). In American roulette,
	there is a second green pocket marked 00. Pocket number order on
	the roulette wheel adheres to the following clockwise sequence in
	most casinos:

	0-28-9-26-30-11-7-20-32-17-5-22-34-15-3-24-36-13-1-
	00-27-10-25-29-12-8-19-31-18-6-21-33-16-4-23-35-14-2

	
	Gameplay
	--------
	
	- the user will begin with an amount of money (say, $10,000) and can
	  place bets (on 1, 2, 3, 4, 5, or 6 numbers, with  payouts of 35 to 1,
	  17 to 1, 11 to 1, 8 to 1, 6 to 1, and 5 to 1, respectively, OR a bet
	  on the first, middle, or last twelve numbers with a payout of 2 to 1)
	- the user can play until they lose all of their money (<= 0) or until
	  they decide to quit
	- at the end of the game, whether they lost or won will be displayed
	  before the window closes
		- user clicks "quit game" button -> if they won money display that
		  they won / if they lost money display that they lost / if they
		  broke even display that they broke even
		- obviously, if the user loses all of their money before quitting,
		  they lost

'''

# import PyQt4 packages
import random


# ------ gameplay, without graphics ------

# main loop (until 'quit game' is selected OR user loses all their money)
	# user selects the type of bet they want to make
	# user selects how much they want to bet
	# wheel is spun (random.randint(1, 38))
	# determine whether user won the bet
	# adjust the amount of money the user has accordingly
