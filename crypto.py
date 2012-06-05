from math import *
import random

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

