import re

with open('input.txt', 'r') as inputFile:
	contents = inputFile.readlines()[0]

	contents = re.sub('!.', '', contents)
	contents = re.sub('<.*?>', '', contents)

	# There's probably a smarter, regex-only way to do this. This is quite 'C'-styley

	depth = 0
	score = 0

	for char in contents:
		if char == '{':
			depth += 1
			score += depth
		elif char == '}':
			depth -= 1
	
	print score