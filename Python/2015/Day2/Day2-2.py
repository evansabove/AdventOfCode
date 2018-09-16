def getShortestPerimeter(l, w, h):
	perimeters = [2*(l+w), 2*(w+h), 2*(h+l)]

	return min(perimeters)

def getBowLength(l, w, h):
	return l*w*h

def parseInput():
	
	with open('input.txt', 'r') as inputFile:
		allLines = inputFile.readlines()

		totalLength = 0
		for line in allLines:
			dimensions = line.split('x')

			totalLength += getShortestPerimeter(int(dimensions[0]), int(dimensions[1]), int(dimensions[2])) + getBowLength(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

			
		print totalLength

parseInput()