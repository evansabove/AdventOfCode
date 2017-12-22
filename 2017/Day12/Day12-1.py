def findPrograms(id):
	global programs, pipes

	pipe = pipes[id]

	programs.append(id)

	children = [int(c.strip()) for c in pipe.split('<->')[1].split(',')]

	for i in [c for c in children if c not in programs]:
		findPrograms(i)


with open('input.txt', 'r') as inputFile:
	pipes = [i.strip() for i in inputFile.readlines()]
	programs = []

	findPrograms(0)

	print len(set(programs))
