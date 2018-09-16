with open('input.txt', 'r') as inputFile:
	list = range(256)
	currentPosition = 0
	skipSize = 0

	lengths = [int(i.strip()) for i in inputFile.readlines()[0].split(',')]

	for length in lengths:
		
		rearranged_list = list[currentPosition:] + list[:currentPosition]
		reversed_list = rearranged_list[:length][::-1] + rearranged_list[length:]
		
		list = reversed_list[len(list)-currentPosition:] + reversed_list[:len(list)-currentPosition]

		currentPosition = (currentPosition + length + skipSize) % len(list)
		skipSize += 1

	print list[0]*list[1]