#!/usr/bin//env python3
# -*- coding:utf_8 -*-
'''
1: black
0: white
一个盒子中有黑子白子，同时取出两个，颜色一样丢弃，不一样，白子放回盒子，并加入一黑子
'''

import random,time

start = time.time()
# initial box
b = int(input('Black Number: '))
w = int(input('White Number: '))
x = [1]*b + [0]*w
print(x)
random.shuffle(x)
print(x)

# loop
i=0
# all black
if w == 0: 
	while len(x) > 1:
		del x[i]  # del:both black and add one means del just one black
# white within 
else:
	while len(x) > 1:
		if x[i] == x[i+1]:  # del both
			del x[i]   
			del x[i+1]
			x.append(1)   # add:black
		elif x[i] == 1:
			del x[i]      #keep white , del black
		else:
			del x[i+1]	 #keep white , del black
print('*'*30)
print('[0]<==>white remained; [1]<==>black remained')
print('The remained one is:\t',x)
print('Time used: %s seconds'%(time.time()-start))
