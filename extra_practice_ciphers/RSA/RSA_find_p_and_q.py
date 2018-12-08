e = 3
n = 294689500

# Initialize a list
primes = []

for possiblePrime in range(2, 100000):
	# Assume number is prime until shown it is not.
	isPrime = True
	for num in range(2, possiblePrime):
		if possiblePrime % num == 0:
			isPrime = False

	if isPrime:
		primes.append(possiblePrime)
		q = n / possiblePrime

		#print(q)
		int_of_q = int(q)
		#print(int_of_q)
		float_of_int_q = float(int_of_q)

		if((q == int_of_q) or (q == float_of_int_q)):
			print('Found')
			print(possiblePrime)
			print(q)
			break

#q = n / p
