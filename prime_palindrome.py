primes = [2]
for n in range(1, 1000):
	for prime in primes:
		if n // prime != n / prime: