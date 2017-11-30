def moveRealSanta(char):
	global santaX, santaY

	if char == '^':
		santaY += 1
	elif char == 'v':
		santaY -= 1
	elif char == '<':
		santaX -= 1
	elif char == '>':
		santaX += 1

	return (santaX, santaY)

def moveRoboSanta(char):
	global roboX, roboY

	if char == '^':
		roboY += 1
	elif char == 'v':
		roboY -= 1
	elif char == '<':
		roboX -= 1
	elif char == '>':
		roboX += 1

	return (roboX, roboY)

santaX = 0
santaY = 0
roboX = 0
roboY = 0

with open('input.txt', 'r') as inputFile:
	allInstructions = inputFile.read()

	visitedLocations = []

	for index, char in enumerate(allInstructions):

		#result = ()
		if(index % 2 == 0):
			result = moveRealSanta(char)
		else:
			result = moveRoboSanta(char)

		if result not in visitedLocations:
			visitedLocations.append(result)

	print len(visitedLocations)