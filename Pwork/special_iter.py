#!/usr/bin/env python3
# coding:utf:8

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 # initialize 0 and 1
		
	def __iter__(self):
		return self           #instance is object for iteration
		
	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 100:
			raise StopIteration();
		return self.a
		
		
for x in Fib():
	print(x)