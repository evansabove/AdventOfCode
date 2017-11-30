# Start at origin x=0,y=0
# Any move up or down (^/v) increments/decrements the y
# Any move left or right (</>) increments/decrements the x
# Keep a log of where you've been


with open('input.txt', 'r') as inputFile:
	allInstructions = inputFile.read()

	visitedLocations = []

	currentX = 0
	currentY = 0

	for char in allInstructions:
		if char == '^':
			currentY += 1
		elif char == 'v':
			currentY -= 1
		elif char == '<':
			currentX -= 1
		elif char == '>':
			currentX += 1

		if (currentX, currentY) not in visitedLocations:
			visitedLocations.append((currentX, currentY))

	print len(visitedLocations)