# Using trial division of integers between 2 and sqrt n
# Starting with lower more probable numbers
#
# Only checks odd numbers
# `primes` counter starts at 1 to include '2' as the first prime

from math import sqrt

target = 10001
primes = 1 
n = 1

while primes < target:
	n += 2
	found = False
	upper = int(sqrt(n)) + 1
	for i in xrange(2, upper):
		if n % i == 0:
			found = True
			break
	
	if not found:
		primes += 1

print n

