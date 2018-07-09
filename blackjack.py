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

		- numeric cards (2-10) are worth their number
		- face cards are worth 10
		- aces are worth 1 or 11, whichever is most helpful

		- if the player's hand exceeds 21, it is a loss
		- elif the dealer's hand exceeds 21, it is a win
		- elif the player's hand is equal to the dealer's hand, it is a tie
		- elif the player's hand is greater than the dealer's hand, it is a win
		- else it is a loss


	remaining implementation
	------------------------
	
		- will use PyQt5 to display a green casino table background as
		  well as each card that the player has/all the cards at the end
		  of a game
		- will display wins/losses/ties/total number of games on the side,
		  and update values as the games go on
		- once player quits game, will display "Congratulations!" or
		  "Better luck next time!" depending on the win/loss ratio

'''

# import PyQt5 packages
import random

# ------ gameplay, without graphics ------


# Calculate total of cards
def score(cards):
	sum = 0
	aceCount = 0
	
	for i in cards:
		if i[0] == "A":
			aceCount += 1
		elif str.isdigit(i[0]):
			if i[0] == "1":
				sum += 10
			else:
				sum += int(i[0])
		else:
			sum += 10

	for i in range(aceCount):
		sum += 1

	for i in range(aceCount):
		if sum + 10 <= 21:
			sum += 10

	return sum


# Deal cards to dealer and player
def deal():
	deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS",
			"QS", "KS", "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H",
			"10H", "JH", "QH", "KH", "AC", "2C", "3C", "4C", "5C", "6C", "7C",
			"8C", "9C", "10C", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D",
			"6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

	playerCards = []
	dealerCards = []
	playerCards.append(deck[random.randint(0, len(deck) - 1)])
	deck.remove(playerCards[0])
	dealerCards.append(deck[random.randint(0, len(deck) - 1)])
	deck.remove(dealerCards[0])
	playerCards.append(deck[random.randint(0, len(deck) - 1)])
	deck.remove(playerCards[1])
	dealerCards.append(deck[random.randint(0, len(deck) - 1)])
	deck.remove(dealerCards[1])

	return deck, dealerCards, playerCards


# Select regular or advanced mode
#	- in regular mode, dealer randomly chooses to hit or stand
# 	- in advanced mode, dealer strategically chooses to hit or stand
mode = int(input("Select a mode:\n0 - Regular\n1 - Advanced\n> "))

# Accounting for invalid input
while mode != 0 and mode != 1:
	mode = int(input("Invalid input. Please enter 0 or 1: "))

choice = "0"
wins = 0; losses = 0; ties = 0

while choice.lower() != "n":

	pIndex = 2
	dIndex = 2

	deck, dCards, pCards = deal()

	gameNotOver = True
	rnd = 1

	while gameNotOver:
		# If in first round or if hit chosen
		if choice.lower() != "s":
			print("\nYour cards: ", end="")
			for i in pCards:
				print(i + " ", end="")
			print()

			choice = input("Hit or stand (H/S)? ")

			# Accounting for invalid input
			while choice.lower() != "s" and choice.lower() != "h":
				choice = input("Invalid input. Enter H or S: ")

		# If hit chosen, give player additional card
		if choice.lower() == "h":
			pCards.append(deck[random.randint(0, len(deck) - 1)])
			deck.remove(pCards[pIndex])
			pIndex += 1

		# If in regular mode and stand was not already randomly chosen,
		# randomly choose between hit and stand
		if mode == 0 and rnd == 1:
			rnd = random.randint(0, 1)

		# If in regular mode and hit was randomly chosen or if in
		# advanced mode and hit is strategically beneficial, give
		# dealer additional card
		if (mode == 0 and rnd == 1) or (score(dCards) < 17 and mode == 1):
			dCards.append(deck[random.randint(0, len(deck) - 1)])
			deck.remove(dCards[dIndex])
			dIndex += 1
		# If dealer was not given additional card, the dealer "picked" stand.
		# If the player also chose stand, the game is over
		else:
			if choice.lower() == "s":
				gameNotOver = False

		# If either player exceeds 21, the game is over	
		if score(pCards) > 21 or score(dCards) > 21:
			gameNotOver = False

	
	print("\nYour cards: ", end="")
	for i in pCards:
		print(i + " ", end="")
	print("\nDealer's cards: ", end="")
	for i in dCards:
		print(i + " ", end="")
	print()

	# Calculate and print card totals
	pScore = score(pCards)
	dScore = score(dCards)

	print("You got: " + str(pScore))
	print("The dealer got: " + str(dScore))

	# Adjust number of wins/losses/ties accordingly
	if pScore > 21:
		print("You lost!")
		losses += 1
	elif pScore > dScore or dScore > 21:
		print("You won!")
		wins += 1
	elif pScore < dScore:
		print("You lost!")
		losses += 1
	elif pScore == dScore:
		print("You tied!")
		ties += 1


	choice = input("Continue (Y/N)? ")

	# Accounting for invalid input
	while choice.lower() != "y" and choice.lower() != "n":
		choice = input("Invalid input. Please enter Y or N: ")


# Print win/loss/tie stats, end game
print("\nWins\tLosses\tTies   | Total")
total = wins + losses + ties
print("-----------------------|------")
print(str(wins) + "\t" + str(losses) + "\t" + str(ties) + "      | " + str(total))


print("\nThanks for playing!")

