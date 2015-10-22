#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name:		Bagels Game
# Date: 	12 Jul 2015
# Author: 	Laury MIAO

import random
#initialize the screen
def ScreenInit():
	print('''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
	When I say: 	That means:\n	
	Pico		One digit is correct but in the wrong position.
	Fermi 		One digit is correct and in the right position.
	Bagels		No digit is correct.
I have thought up a number. You have 10 guesses to get it.
	''')

# generate number :m <= number <= n
def getRandInt(m,n): 
	return random.randint(m,n)

#get the digit numbers
def getDigit(num):
	a = []
	while num!=0:
		a.append(num%10) #store the last digit to a
		num //= 10		# update num without the last digit
	a.reverse()
	return a

#judge : output Fermi, Pico, Bagels in a string
def judgeDigits(a, b): # a,b must be the same length
	result = ''
	if len(a) != len(b):
		print('the two list are not in the same length')
		return None
	for i in range(len(a)):
		if a[i] in b:
			if a[i] == b[i]:
				result += ' Fermi'
			else:
				result += ' Pico'
		else:
			result += ' Bagels'
	return result

#get guess from the player
def getGuess(num):
	s = input()
	while len(s) != len(str(num)):
		print('Enter again:')
		s = input()
	return int(s)
	
	
ScreenInit()

secret_number = getRandInt(100,999)
secret_digit = getDigit(secret_number)
guess_aim = ''
for i in range(len(secret_digit)):
	guess_aim += ' Fermi'
#print(guess_aim)
for guess_count in range(1,11): # less than 10 times
	guess_number = getGuess(secret_number)
	guess_digit = getDigit(guess_number)
	compare = judgeDigits(guess_digit, secret_digit)
	print('Guess #',guess_count)
	print(compare)
	new_com = compare.split()
	print(new_com)
	bo = True
	for n_com in new_com:
		if n_com != 'Fermi':
			bo = False
	if bo:
		print('You have got the right number')
		break