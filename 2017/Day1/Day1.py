with open('input.txt', 'r') as inputFile:
	allLines = inputFile.read()

	# Loop over all digits
	# If digit i == digit i+1
		# total += digit

	total = 0

	if allLines[0] == allLines[-1]:
		total += int(allLines[0])

	for index, value in enumerate(allLines):

		if(index == len(allLines)-1):
			break

		if value == allLines[index+1]:
			total += int(value)

	print total