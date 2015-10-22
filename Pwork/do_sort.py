#!/usr/bin//env python3
# -*- coding:utf_8 -*-

import time
import random
start = time.clock()
n = int(input('Input the number u wanna arrange (N): '))
i = int(input('Input the number u wanna arrange (i, i <= N): '))
a =[] # initial list empty
# generate the random list
for x in range(n):
	a.append(random.randint(0,n+1))
	
if i in range(n+1):
#	a = list(range(n))
	x = a[:i:]
	y = a[i::]
	b = y+x
	print(a)
	print()
	print(b)
	end = time.clock()
	print('Time running:%f ' % (end - start))
else:
	print('Wrong number : %d' %i)
	
