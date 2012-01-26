# using trial division of integers between 2 and sqrt n
# starting with lower more probable numbers

from math import sqrt

target = 10001
primes = 0
n = 1

while primes < target:
	n += 1
	found = False
	upper = int(sqrt(n)) + 1
	for i in xrange(2, upper):
		if n % i == 0:
			found = True
			break
	
	if not found:
		primes += 1

print n

