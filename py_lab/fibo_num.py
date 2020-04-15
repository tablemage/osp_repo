#!/usr/bin/python3

F=[1,1]
n=int(input('fibonacci number?'))
if n<3:
	for i in range(n):
		print('%d '%F[i], end='')
	print('')
else:
	for i in range(2,n):
		F.append(F[i-1]+F[i-2])
	for i in range(n):
		print('%d '%F[i], end='')
	print('')

print('F%d = %d'%(n,F[n-1]))
