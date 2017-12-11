def conditionTrue(arg1, op, arg2):
	global registers


	arg1Value = [i for i in registers if i['name'] == arg1][0]['value']

	if op == '<':
		#print str(arg1Value) + '<' + arg2
		return arg1Value < int(arg2)
	if op == '>':
		#print str(arg1Value) + '>' + arg2
		return arg1Value > int(arg2)
	if op == '==':
		#print str(arg1Value) + '==' + arg2
		return arg1Value == int(arg2)
	if op == '<=':
		#print str(arg1Value) + '<=' + arg2
		return arg1Value <= int(arg2)
	if op == '>=':
		#print str(arg1Value) + '>=' + arg2
		return arg1Value >= int(arg2)
	if op == '!=':
		#print str(arg1Value) + '!=' + arg2
		return arg1Value != int(arg2)

with open('input.txt', 'r') as inputFile:
	instructions = [i.rstrip() for i in inputFile.readlines()]

	registers = []

	for i in instructions:
		parts = i.split(' ')

		if parts[0] not in [r['name'] for r in registers]:
			registers.append({'name': parts[0], 'value': 0})

	highestValueEver = 0

	for i in instructions:
		parts = i.split(' ')

		register = next(i for i in registers if i['name'] == parts[0])

		if conditionTrue(parts[4], parts[5], parts[6]):
			if parts[1] == 'inc':
				register['value'] += int(parts[2])

				if register['value'] > highestValueEver:
					highestValueEver = register['value']

			if parts[1] == 'dec':
				register['value'] -= int(parts[2])

				if register['value'] > highestValueEver:
					highestValueEver = register['value']

	print 'Max val: ' + str(max([i['value'] for i in registers]))
	print 'Highest value ever: ' + str(highestValueEver)

