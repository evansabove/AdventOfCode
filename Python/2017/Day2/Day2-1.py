with open('input.txt', 'r') as inputFile:
	allLines = inputFile.readlines()

	total = 0
	for line in allLines:
		lineValues = [int(i) for i in line.split('\t')]

		val = max(lineValues) - min(lineValues)
		total += val

	print total