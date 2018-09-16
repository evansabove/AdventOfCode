def makeProgramDict(line):
	splitLine = line.split(' ')

	program = { "name": splitLine[0], "weight": int(splitLine[1].replace('(','').replace(')', '')) }

	if '->' in line:
		childString = line.split('->')[1].strip()

		program["children"] = [{"name": child.strip()} for child in childString.split(',')]

	else:
		program["children"] = []

	return program

def getWeight(programName, programs):
	for i in programs:
		if i["name"] == programName:
			return i["weight"]

def getChildren(programName, programs):
	for i in programs:
		if i["name"] == programName:
			if "children" in i:
				return i["children"]
			else:
				return []

#def calculateTowerWeights(programs):
	#for program in programs:
		#program["totalWeight"] = program["weight"] + sum(getWeight(j["name"], programs) for j in program["children"])
		#program["totalWeight"] = program["weight"] + sum(calculateTowerWeights())

def getTotalWeight(programs, program):
	return getWeight(program["name"], programs) + sum([getTotalWeight(programs, p) for p in getChildren(program["name"], programs)])

def getUnbalancedChildren(program, programs):
	print [getTotalWeight(programs, program) for i in program["children"]]

with open('input.txt', 'r') as inputFile:
	input = inputFile.readlines()

	programs = [makeProgramDict(line) for line in input]

	allChildren = []

	
	#for i in programs:
		#i["totalWeight"] = getTotalWeight(programs, i)
		#print i


	# Starting at our known base program tknk

	#baseProgram = [i for i in programs if i["name"] == 'tknk'][0]
	#print baseProgram

	# Go through all programs that have children
	# Calculate the total weight for all of the children - see if any are mismatched

	for i in programs:
		if len(i["children"]) == 0:
			continue

		values = [getTotalWeight(programs, l) for l in i["children"]]
		if len(set(values)) > 1:
			print values
			differenceNeedsToBe = max(values) - min(values)
			print "Difference needs to be " + str(differenceNeedsToBe) + " on " + i["name"]
			childWeights = [getWeight(c["name"], programs) for c in i["children"]]

			indexToReduce = values.index(max(values))

			resultingWeight = childWeights[indexToReduce] - differenceNeedsToBe

			print resultingWeight


			#print pairs of values, weights of children



			#originalWeights = [getWeight(c["name"], programs) for c in i["children"]]
			#print originalWeights



			





	#getUnbalancedChildren(baseProgram, programs)