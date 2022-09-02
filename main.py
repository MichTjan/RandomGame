import sys, random

sys.argv

def playagain():
	playagain = input("Would you like to play again? Yes or No? ")
	if playagain.lower() == "yes":
		randomgame()
	elif playagain.lower() == "no":
		print("We hope to see you again! Bye!")
	elif playagain != "no" or playagain != "yes":
		print("It's Yes or No! Bye!")

def randomgame():
	random_number = random.randint(1,10)
	guess = input("Guess a number between 1-10: ")

	if guess.isdigit():
		if guess == random_number:
			print("You got it!")
		elif 1 > int(guess) > 10:
			print("Oops! The number you wrote is not within range.")
		elif guess != random_number:
			print("Try again!")
			playagain()

	else:
		print("That's not an integer.")
		randomgame()

randomgame()