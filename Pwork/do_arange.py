#!/usr/bin//env python3
# -*- coding:utf_8 -*-

a = list(range(11,20))
b = list(range(1,10))
c = (a+b)
c.sort(reverse=True)
print(c)
x = []
y = []
for i in range(len(c)-1):
	if i in a:
		x.append(i)
	else:
		y.append(i)