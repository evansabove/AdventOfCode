def makePass(delay, layers, depths):

	lastLayer = max(depths)

	caught = False

	for layer in range(lastLayer+1):

		if layer not in depths:
			continue

		thisLayer = [l for l in layers if l['depth'] == layer][0]
		period = (2*thisLayer['range'])-2

		caught = (layer+delay) % period == 0 or caught

	return caught


with open('input.txt', 'r') as inputFile:
	contents = [i.strip() for i in inputFile.readlines()]

	layers = []
	for i in contents:
		splitLine = i.split(':')

		layers.append({ 'depth': int(splitLine[0]), 'range': int(splitLine[1])})

	depths = [l['depth'] for l in layers]

	testDelay = 0
	while True:
		caught = makePass(testDelay, layers, depths)

		if not caught:
			break

		testDelay = testDelay + 1

		if testDelay % 1000 == 0:
			print testDelay

	print testDelay