with open('input.txt', 'r') as inputFile:
	contents = inputFile.readlines()

	validCount = 0
	for i, line in enumerate(contents):

		words = line.rstrip().split(' ')

		if len(words) == len(set(words)):
			validCount += 1

	print validCount


	