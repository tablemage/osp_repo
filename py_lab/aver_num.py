#!/usr/bin/python3

a=0
n=int(input('how many number will you calculate?: '))
for i in range(n):
	b=int(input('input number: '))
	a=a+b

c=a/n
print('Average is: %d'%(c))
