from itertools import cycle

def reallocate(banks):

	biggestValue = max(banks)
	biggestValueIndex = banks.index(biggestValue)

	shiftedList = banks[biggestValueIndex+1:] + banks[:biggestValueIndex+1]
	shiftedList[-1] = 0

	bankCycle = cycle(enumerate(shiftedList))

	while biggestValue > 0:

		shiftedList[next(bankCycle)[0]] += 1

		biggestValue -= 1

	return shiftedList[len(shiftedList)- biggestValueIndex-1:] + shiftedList[:len(shiftedList)- biggestValueIndex-1]

with open('input.txt', 'r') as inputFile:
	banks = [int(i) for i in inputFile.read().split('\t')]

	seenCombinations = []
	seenCombinations.append(banks)

	while True:
		thisResult = reallocate(banks)

		if thisResult in seenCombinations:
			break;

		seenCombinations.append(thisResult)

		banks = thisResult

	print len(seenCombinations)

	
	
