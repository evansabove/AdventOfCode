import itertools

def isAnagramOf(a, b):
	if len(a) != len(b):
		return False

	a = ''.join(sorted(a))
	b = ''.join(sorted(b))

	for i in range(len(a)):
		if a[i] != b[i]:
			return False

	return True

with open('input.txt', 'r') as inputFile:
	contents = inputFile.readlines()

	validCount = 0
	for i, line in enumerate(contents):

		words = line.rstrip().split(' ')

		lineHasAnagrams = False
		for a,b in itertools.combinations(words, 2):
			lineHasAnagrams = lineHasAnagrams or isAnagramOf(a, b)

		if not lineHasAnagrams:
			validCount += 1

	print validCount

