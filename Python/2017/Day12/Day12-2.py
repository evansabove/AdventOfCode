def findPrograms(id):
	global programs, pipes

	pipe = pipes[id]

	programs.append(id)

	children = [int(c.strip()) for c in pipe.split('<->')[1].split(',')]

	for i in [c for c in children if c not in programs]:
		findPrograms(i)

def findGroups():
	global programs, programCount

	remainingPrograms = range(programCount)

	group = 0
	groupCount = 0
	
	while len(remainingPrograms) > 0:
		findPrograms(group)
		groupCount = groupCount + 1

		remainingPrograms = [i for i in range(programCount) if i not in programs]

		if len(remainingPrograms) > 0:
			group = remainingPrograms[0]


	return groupCount


with open('input.txt', 'r') as inputFile:
	pipes = [i.strip() for i in inputFile.readlines()]

	programCount = int(pipes[-1].split(' ')[0])+1

	programs = []

	print findGroups()