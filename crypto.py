from math import *
import random

# From http://www.stealthcopter.com/blog/2009/11/python-factors-of-a-number/
def factor(n):
	n = int(n)
	
	# 1 and n are automatically factors of n
	fact=[1, n]
	# starting at 2 as we have already dealt with 1
	check=2
	# calculate the square root of n and use this as the
	# limit when checking if a number is divisible as
	# factors above sqrt(n) will already be calculated as
	# the inverse of a lower factor IE. finding factors of
	# 100 only need go up to 10 (sqrt(100)=10) as factors
	# such as 25 can be found when 5 is found to be a
	# factor 100/5=25
	rootn=sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	# this line checks the sqrt of the number to see if
	# it is a factor putting it here prevents it appearing
	# twice in the above while loop and putting it outside
	# the loop should save some time.
	if rootn==check:
		fact.append(check)
		# return an array of factors sorted into numerial order.
        fact.sort()
	return fact


# This function calculates the inverse of an element b mod n
# It uses the extended euclidean algorithm
def invmodn(b, n):
	n0 = int(n)
	b0 = int(b % n)
	t0 = 0L
	t  = 1L

	q = int(n0/b0)
	r = n0 - q * b0;
	while r > 0:
		temp=t0-q*t;
		if (temp >= 0):
			temp = (temp % n)
		if (temp < 0):
			temp = n - (-temp %n)
		t0=t
		t=temp
		n0=b0
		b0=r
		q=int(n0/b0);
		r=n0-q*b0;

	if b0 != 1:
		return None
	else:
		return (t % n)

# This function calculates y = a^z mod n
def powermod(a, z, n):
	# If a is negative, put it back to between 0 and n-1
	a = int(a % n)
	z = int(z)
	n = int(n)

	# Take care of any cases where the exponent is negative
	if z < 0:
		z = -z
		a = invmodn(a, n)
		if a == None:
			return None
	
	x = 1
	a1 = a
	z1 = z
	while (z1 != 0):
		while (z1 % 2) == 0:
			z1 = int(z1 / 2)
			a1 = ((a1 * a1) % n)
		
		z1 = z1 - 1
		x  = x * a1
		x  = (x % n)
	
	return x

# Calculates the Euler phi function of n
def eulerphi(n):
	f   = factor(n)
	f.append(0) # Appending a zero to make (f(j)==f(j+1)) never go out of bounds

	phi = 1
	ct  = 0
	for j in range(1, len(f) - 1):
		if (f[j]==f[j+1]):
			ct = ct + 1 # count number of times a factor occurs
		else:
			phi = phi * f[j]^ct
			phi = phi * (f[j] - 1)
			ct=0
			
	return phi

# This function solves the Chinese Remainder Theorem problem:
#   x= a(1) mod m(1)
#   x= a(2) mod m(2)
#   ...
#   x= a(r) mod m(r)
# The values for a and m should be a vector of the same dimension
def crt(a, m):
	if len(a) != len(m):
	   raise Exception('The vectors a and m should be the same size')

	M = 1
	for x in m:
		M *= x

	x = 0

	for j in range(0, len(a)):
	   x = (x + a[j] * (M / m[j]) * invmodn(M/m[j], m[j])) % M
	
	return x