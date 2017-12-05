with open('input.txt', 'r') as inputFile:
	jumps = [int(i) for i in inputFile.readlines()]

	jumpCount = 0
	position = 0
	while position < len(jumps) and position >= 0:
		originalInstruction = jumps[position]		
		jumps[position] += -1 if originalInstruction >= 3 else 1

		position += originalInstruction
		jumpCount += 1

	print jumpCount