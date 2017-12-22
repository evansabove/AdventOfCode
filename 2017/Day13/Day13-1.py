def makePass(time, layers):

	lastLayer = int(layers[-1].split(':')[0])+1

	severity = 0

	for layer in range(lastLayer):

		if layer not in [int(l.split(':')[0]) for l in layers]:
			time = time + 1
			continue

		thisLayer = [l for l in layers if l.split(':')[0] == str(layer)][0]

		depth = int(thisLayer.split(':')[0].strip())
		wallRange = int(thisLayer.split(':')[1].strip())

		period = (2*wallRange)-2

		if time % period == 0:
			severity = severity + (depth * wallRange)

		time = time + 1

	return severity


with open('input.txt', 'r') as inputFile:
	layers = [i.strip() for i in inputFile.readlines()]

	bestSeverity = 99999
	time = 0

	while bestSeverity != 0:
		result = makePass(time, layers)

		if result < bestSeverity:
			bestSeverity = result
			print bestSeverity

		time += 1

	print result




	#while bestSeverity != 0:
		#result = makePass(time, layers)
#
		#print result
#
		#if result < bestSeverity:
			#bestSeverity = result
#
		#time += 1

	print 'Delay: ' + str(time)
