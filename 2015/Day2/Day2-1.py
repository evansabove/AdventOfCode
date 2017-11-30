def getRequiredArea(l, w, h):

	values = [2*l*w, 2*w*h, 2*h*l]

	return sum(values) + (min(values))/2

def parseInput():
	
	with open('input.txt', 'r') as inputFile:
		allLines = inputFile.readlines()

		total = 0
		for line in allLines:
			dimensions = line.split('x')
			total += getRequiredArea(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

		print total

parseInput()