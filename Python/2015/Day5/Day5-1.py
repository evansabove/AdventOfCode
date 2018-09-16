def containsThreeVowels(input):
	return len([i for i in input if i in ['a','e','i','o','u']]) >= 3

def hasDoubleLetter(input):
	for i, char in enumerate(input):
		if i+1 >= len(input):
			return False

		if char == input[i+1]:
			return True

	return False

def hasNoForbiddenStrings(input):
	for i in ['ab', 'cd', 'pq', 'xy']:
		if i in input:
			return False

	return True


with open('input.txt', 'r') as inputFile:
	allStrings = inputFile.readlines()

	print len([i for i in allStrings if containsThreeVowels(i) and hasDoubleLetter(i) and hasNoForbiddenStrings(i)])

