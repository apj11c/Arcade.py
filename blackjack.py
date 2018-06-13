''' blackjack.py

	simple blackjack gameplay
	-------------------------

		- "hit" (accept another card) and "stand" (do not accept another card)
		  are the only options as this is a more casual game of blackjack
		  rather than one you would find in a casino
		- no betting, just keeps track of wins/losses/ties
		- only one opponent
		- user can continue playing rounds until they quit
		- played with one deck of cards
		- score is kept for both user and dealer

		- if the player's hand exceeds 21, it is a loss
		- elif the dealer's hand exceeds 21, it is a win
		- elif the player's hand is equal to the dealer's hand, it is a tie
		- elif the player's hand is greater than the dealer's hand, it is a win
		- else it is a loss
		
		- if the round was a tie, ties += 1 for dealer and player
		- elif the winner's hand was exactly 21,
		  wins += 2 for the winner
		- else wins += 1 for winner, losses += 1 for loser

		- potential for increased difficulty level:
			- play with > 1 deck of cards
			- 'regular' mode where dealer chooses hit/stand randomly and
			  'advanced' mode where dealer is smarter about hit/stand
'''

# import PyQt4 packages
import random


# ------ gameplay, without graphics ------

dealerWins = 0; dealerLosses = 0; dealerTies = 0
userWins = 0; userLosses = 0; userTies = 0

# main loop (until 'quit game' is selected)
# user plays against the house/dealer (i.e. only one opponent)
	# deal user two random cards (random.randint(1, numDecks * 52))
	# ask user if they want another card ("hit me"/"stand" buttons)
	# house makes either random or smart choice about being dealt another card
	# when both the user and the house pass ("stand"), the round is over
	# dealer's cards are revealed
	# increment wins/losses/ties accordingly

