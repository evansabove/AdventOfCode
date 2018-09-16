def doKnotHash(arr):
	global list

	currentPosition = 0
	skipSize = 0

	for item in arr:
		rearranged_list = list[currentPosition:] + list[:currentPosition]
		reversed_list = rearranged_list[:item][::-1] + rearranged_list[item:]
		
		list = reversed_list[len(list)-currentPosition:] + reversed_list[:len(list)-currentPosition]

		currentPosition = (currentPosition + item + skipSize) % len(list)
		print currentPosition

		skipSize += 1


def xorList(lis):
	return reduce(lambda a, b: int(a) ^ int(b), lis)


def doDenseHash(lis):
	return [xorList(lis[x*16:((x+1)*16)]) for x in range(16)]

lengths = [ord(i) for i in '1,2,3']

list = range(256)

doKnotHash(lengths)

denseHash = doDenseHash(list)

print denseHash

print ''.join(['{:02x}'.format(x) for x in denseHash])