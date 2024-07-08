from time import sleep
import random

correctNumber = random.randint(1, 10)
attempts = 1

print('Welcome to numGuesser (name change pending)!')
sleep(2)
print('I will think of a number from 1-10, and if you guess it correctly, you win!')
sleep(2)


def badGuess():
	print('Incorrect, try again.')
	sleep(1)


def goodGuess():
	print('That is correct, well done!')
	sleep(1)
	print('You took', attempts, 'attempts!')


while True:
	playerGuess_str = input('What number am I thinking of?: ')
	playerGuess = int(playerGuess_str)
	if playerGuess != correctNumber:
		sleep(1)
		badGuess()
		attempts = attempts + 1

	else:
		sleep(1)
		goodGuess()
		sleep(2)
		break

while True:
	exitToken = input('Enter any key to close the program. ')
	leave = True
	if leave is True:
		break

quit()
