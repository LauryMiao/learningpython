#!/usr/bin//env python3
# -*- coding:utf_8 -*-

# 二分法
# 数组已排序，升序
#未升序可用sort方法

#------------------------------------------------------------
def find_2d(t,arr):      #寻找t
	low = -1
	up = len(arr)
	p = {}                # 储存寻找元素t的dict
	
	while low+1 != up:
		m = (low+up)//2
		if t < arr[m]:    # t in low-m
			up = m
		elif t == arr[m]: #找到，移到dict p ， 删除arr[m]，继续
			p[m]=t
			break         # 跳出循环，进行左右search
		else:#t > arr[m]: # t in m-up
			low = m
#------------------------------------------------------------
	i = 1                 #向右搜寻
	while i < up-m:		 #i: m....up-m
		if arr[m+i] == t:
			p[m+i]=t
		else:
			break
		i += 1
#------------------------------------------------------------		
	j = 1				 #向左搜寻
	while j < m-low:	#j :1....m-low
		if arr[m-j] == t:
			p[m-j]=t
		else:
			break
		j += 1
#------------------------------------------------------------	
	if len(p) == 0:
		print(t,' doesn\'t exist in the array')
	else:
		print(p)
	print('*'*40)
#------------------------------------------------------------		
arr = list(range(10))	
find_2d(5,arr)
find_2d(200,arr)
arr = [1,2,5,5,88,5,99,22]
arr.sort() #排序
find_2d(5,arr)