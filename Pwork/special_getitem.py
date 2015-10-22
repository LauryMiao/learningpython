#!/usr/bin/env python3
# coding:utf-8

class Fib(object):
	
	def __getitem__(self, n):
		if isinstance(n, int):			# n is int
			a, b = 1, 1
			if n > 2:
				for x in range(n):
					a, b = b, a+b
			return a
			
		if isinstance(n, slice):		# n is slice
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			
			if stop > 2:
				for x in range(start): # before start, calculte
					a, b = b, a+b
				for x in range(stop):  # start~stop, tally and calculte
					L.append(a)
					a, b = b, a+b
					
			return L		
			
	
f=Fib()
print(f[0])
print(f[1])
print(f[5])
print(f[100])
print(f[:5])
print(f[5:10])