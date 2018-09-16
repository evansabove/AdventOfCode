def doKnotHash(lengths):
	global list, currentPosition, skipSize

	for length in lengths:
		
		rearranged_list = list[currentPosition:] + list[:currentPosition]
		reversed_list = rearranged_list[:length][::-1] + rearranged_list[length:]
		
		list = reversed_list[len(list)-currentPosition:] + reversed_list[:len(list)-currentPosition]

		currentPosition = (currentPosition + length + skipSize) % len(list)
		skipSize += 1


def xorList(lis):
	return reduce(lambda i, j: int(i) ^ int(j), lis)


def doDenseHash(lis):
	return [xorList(lis[x*16:((x+1)*16)]) for x in range(16)]


with open('input.txt', 'r') as inputFile:

	lengths = [ord(i) for i in inputFile.readlines()[0]]

	lengths = lengths + [17, 31, 73, 47, 23]

	currentPosition = 0
	skipSize = 0

	list = range(256)

	for i in range(64):
		doKnotHash(lengths)

	denseHash = doDenseHash(list)

	print ''.join(['{:02x}'.format(x) for x in denseHash])