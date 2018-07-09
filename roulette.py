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
	  17 to 1, 11 to 1, 8 to 1, 6 to 1, and 5 to 1, respectively
	- the user can play until they lose all of their money or until
	  they decide to quit
	- at the end of the game, whether they lost or won will be displayed
	  before the window closes
		- user clicks "quit game" button -> if they won money display that
		  they won / if they lost money display that they lost / if they
		  broke even display that they broke even
		- obviously, if the user loses all of their money before quitting,
		  they lost

	
	Remaining Implementation
	------------------------
	
	- Will use PyQt5 to display roulette wheel
	- Will keep track of winnings on the side, update value as the game goes on
	- Will display numbers bet on and result of spin as well	

'''

# import PyQt5 packages
import random 

# ------ gameplay, without graphics ------

wheel = {0 : "0", 1 : "28", 2 : "9", 3 : "26", 4 : "30", 5 : "11",
		 6 : "7", 7 : "20", 8 : "32", 9 : "17", 10 : "5", 11 : "22",
		 12 : "34", 13 : "15", 14 : "3", 15 : "24", 16 : "36", 17 : "13",
		 18 : "1", 19 : "00", 20 : "27", 21 : "10", 22 : "25", 23 : "29",
		 24 : "12", 25 : "8", 26 : "19", 27 : "31", 28 : "18", 29 : "6",
		 30 : "21", 31 : "33", 32 : "16", 33 : "4", 34 : "23", 35 : "35",
		 36 : "14", 37 : "2"}


# Player starts with $10,000
money = 10000

# Respective returns on betting on 1, 2, 3, 4, 5, or 6 numbers
odds = [35, 17, 11, 8, 6, 5]

print("Current Balance: $" + str(money))

choice = int(input("How many numbers do you want to bet on (1-6, 0 to quit)? "))

# Accounting for invalid input
while choice < 0 or choice > 6:
	choice = int(input("Please enter a number 1-6 (0 to quit): "))


# If 0 is chosen, quit game
while choice != 0:
	betAmt = int(input("How much do you want to bet? "))

	# Accounting for invalid input
	while betAmt > money or betAmt < 0:
		print("Invalid bet amount (valid amounts are 1-" + str(money) + ").")
		betAmt = int(input("How much do you want to bet? "))


	nums = []
	
	# Placing bets
	print("Enter the numbers:")
	for i in range(0, choice):
		bet = input("Number " + str(i + 1) + ": ")
		
		# Accounting for invalid input
		if ((int(bet) < 0 or int(bet) > 36) and bet != "00") or bet in nums:
			while ((int(bet) < 0 or int(bet) > 36)
					and bet != "00") or bet in nums:
				if bet in nums:
					print(bet + " already used.")
				print("Please enter a valid roulette wheel number (0-36 and 00).")
				bet = input("Number " + str(i + 1) + ": ")

	
		nums.append(bet)

	# Spin wheel
	result = random.randint(0, 37)
	
	print("Result: " + wheel[result])

	# Adjust player's money accordingly
	if wheel[result] in nums:
		print("You won!")
		money += (odds[choice - 1] * betAmt)
	else:
		print("You lost!")
		money -= betAmt

	# Game is over if player runs out of money
	if money == 0:
		print("You ran out of money to bet! Game Over.")
		break


	print("Current Balance: $" + str(money))

	choice = int(input("How many numbers do you want to bet on (1-6, 0 to quit)? "))

	while choice < 0 or choice > 6:
		choice = int(input("Please enter a number 1-6 (0 to quit): "))


# Print whether user won or lost money overall
if money > 10000:
	print("You made money! You won!!!")
elif money == 10000:
	print("You didn't lose money! That's a win in my book.")
else:
	print("You lost money! You lose!!!")

