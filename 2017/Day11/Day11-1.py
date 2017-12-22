def move(direction):
	global currentX, currentY

	if direction == 'n':
		currentY = currentY + 2

	elif direction == 'ne':
		currentX = currentX + 1
		currentY = currentY + 1

	elif direction == 'se':
		currentX = currentX + 1	
		currentY = currentY - 1

	elif direction == 's':
		currentY = currentY - 2

	elif direction == 'sw':
		currentX = currentX - 1	
		currentY = currentY - 1

	elif direction == 'nw':
		currentX = currentX - 1	
		currentY = currentY + 1

	else:
		print direction


def cubeDistance(x, y):
	return (abs(x) +abs(y)) / 2

with open('input.txt', 'r') as inputFile:
	directions = inputFile.readline().split(',')

	currentX = 0
	currentY = 0

	furthestFromHome = 0

	for i in directions:
		move(i)

	print cubeDistance(currentX, currentY)

