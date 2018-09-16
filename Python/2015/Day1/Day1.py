# Part 1
with open('input.txt', 'r') as inputFile:
	inputData = inputFile.read()

	countLeft = len([i for i, letter in enumerate(inputData) if letter == '('])
	countRight = len([i for i, letter in enumerate(inputData) if letter == ')'])
	
	print "Part 1: " + str(countLeft - countRight)


# Part 2
with open('input.txt', 'r') as inputFile:
	inputData = inputFile.read()

	currentFloor = 0
	for index, char in enumerate(inputData):
		if char == '(':
			currentFloor += 1
		elif char == ')':
			currentFloor -= 1

		if(currentFloor == -1):
			print "Part 2: " + str(index+1)
			break


