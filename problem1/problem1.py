# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# basic

answer = 233168

result = 0
for i in xrange(1000):
	if not i % 3 or not i % 5:
		result += i

assert result == answer

# using sum
assert answer == sum(filter(lambda x: not x % 3 or not x % 5, xrange(1000)))

# using list comprehension
assert answer == sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])

print 'done'
