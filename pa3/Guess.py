# Kevin Loi
# kloi@ucsc.edu
# pa1
# Generates random number for user to guess

import random

randInt = random.randint(1, 10)

print("")
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")
print("")

firstGuess = input("Enter your first guess: ")

if firstGuess > randInt:
	print("Your guess is too high.")
	print("")
	secondGuess = input("Enter your second guess: ")
	if secondGuess > randInt:
		print("Your guess is too high.")
		print("")
		thirdGuess = input("Enter your third guess: ")
		if thirdGuess > randInt:
			print("Your guess is too high.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		elif thirdGuess < randInt:
			print("Your guess is too low.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		else:
			print("You win!")
			print("")
	elif secondGuess < randInt:
		print("Your guess is too low.")
		print("")
		thirdGuess = input("Enter your third guess: ")
		if thirdGuess > randInt:
			print("Your guess is too high.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		elif thirdGuess < randInt:
			print("Your guess is too low.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		else:
			print("You win!")
			print("")
	else:
		print("You win!")
		print("")
elif firstGuess < randInt:
	print("Your guess is too low.")
	print("")
	secondGuess = input("Enter your second guess: ")
	if secondGuess > randInt:
		print("Your guess is too high.")
		print("")
		thirdGuess = input("Enter your third guess: ")
		if thirdGuess > randInt:
			print("Your guess is too high.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		elif thirdGuess < randInt:
			print("Your guess is too low.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		else:
			print("You win!")
			print("")
	elif secondGuess < randInt:
		print("Your guess is too low.")
		print("")
		thirdGuess = input("Enter your third guess: ")
		if thirdGuess > randInt:
			print("Your guess is too high.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		elif thirdGuess < randInt:
			print("Your guess is too low.")
			print("")
			print("You lose. The number was " +str(randInt))
			print("")
		else:
			print("You win!")
			print("")
	else:
		print("You win!")
		print("")
else:
	print("You win!")
	print("")