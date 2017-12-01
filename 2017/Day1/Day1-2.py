with open('input.txt', 'r') as inputFile:
	allLines = inputFile.read()

	#Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. 
	#That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward 
	#matches it. Fortunately, your list has an even number of elements.

	halfListLength = len(allLines)/2
	total = 0

	for index, value in enumerate(allLines):

		targetIndex = index+halfListLength
		if(targetIndex >= len(allLines)):
			targetIndex -= len(allLines)

		if value == allLines[targetIndex]:
			total += int(value)

	print total