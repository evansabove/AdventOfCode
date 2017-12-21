with open('input.txt', 'r') as inputFile:
	list = range(256)
	currentPosition = 0
	skipSize = 0

	lengths = [int(i.strip()) for i in inputFile.readlines()[0].split(',')]

	for length in lengths:
		print 'starting with: ' + str(list)
		print 'length: ' + str(length)
		print 'currentPosition: ' + str(currentPosition)
		print 'skipSize: ' + str(skipSize)

		
		rearranged_list = list[currentPosition:] + list[:currentPosition]
		print 'to reverse: ' + str(rearranged_list[:length])
		print 'rearranged_list: ' + str(rearranged_list)

		reversed_list = rearranged_list[:length][::-1] + rearranged_list[length:]
		print 'reversed_list: ' + str(reversed_list)

		list = reversed_list[len(list)-currentPosition:] + reversed_list[:len(list)-currentPosition]
		print 'reconstructed list: ' + str(list)

		currentPosition = (currentPosition + length + skipSize) % len(list)
		skipSize += 1

		print '\n'

	print list

	print list[0]*list[1]