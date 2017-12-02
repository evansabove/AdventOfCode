import itertools

with open('input.txt', 'r') as inputFile:
	allLines = inputFile.readlines()

	total = 0
	for line in allLines:
		lineValues = [int(i) for i in line.split('\t')]

		for a,b in itertools.combinations(lineValues, 2):
			if a % b == 0:
				total += a/b
				print a/b
			elif b % a == 0:
				total += b/a
				print b/a

	print total