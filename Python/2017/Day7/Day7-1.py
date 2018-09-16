def makeProgramDict(line):
	splitLine = line.split(' ')

	program = { "name": splitLine[0] }

	if '->' in line:
		childString = line.split('->')[1].strip()

		program["children"] = [{"name": child.strip()} for child in childString.split(',')]

	else:
		program["children"] = []

	return program

with open('input.txt', 'r') as inputFile:
	input = inputFile.readlines()

	programs = [makeProgramDict(line) for line in input]

	allChildren = []

	for i in programs:
		for p in i["children"]:
			if p not in allChildren:
				allChildren.append(p)


	#print allChildren
	#print programs 

	print set([i["name"] for i in allChildren]).symmetric_difference(set([i["name"] for i in programs]))

	#print len(allChildren)
	#print len([i["name"] for i in programs if i not in allChildren])