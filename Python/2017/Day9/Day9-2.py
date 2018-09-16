import re

with open('input.txt', 'r') as inputFile:
	contents = inputFile.readlines()[0]

	escapedContents = re.sub('!.', '', contents)
	garbageGroups = re.findall('<.*?>', escapedContents)

	print len(''.join(garbageGroups)) - 2 * len(garbageGroups)
