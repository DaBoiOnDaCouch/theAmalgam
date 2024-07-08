from time import sleep
from random import uniform


# Adds a blank line to the terminal for better readability
def blankSpace():
	print(' ')


print('Enter the name of a txt file, and its contents will display here, type "quit" at any time to close the program.')
sleep(3)
print('Recently opened files will appear below sorted from oldest to newest')
blankSpace()


recentlyOpened = list()


while True:
	def errWarning():
		print('Name not recognized - file either doesnt exist or the name was typed incorrectly')
		recentlyOpened.remove(fileName)

	# Print the list to console
	def fileList():
		print('Recently opened files:')
		print(recentlyOpened)
		blankSpace()

	blankSpace()
	fileName = input('File name: ')
	fileList()
	if fileName not in recentlyOpened:
		recentlyOpened.append(fileName)

	try:
		fileHandle = open(fileName, 'r')
		for line in fileHandle:
			print(line.strip())
			# Random delay
			ranTime = uniform(0.1, 1.0)
			sleep(ranTime)

	except:
		# Close the program if user types 'quit', otherwise, errWarning()
		if fileName == 'quit':
			break
		errWarning()

quit()
