import hashlib

input = 'bgvyzdsv'

counter = 0
while True:
	result = hashlib.md5(input + str(counter)).hexdigest()

	if result.startswith('000000'):
		print counter
		break

	counter += 1
