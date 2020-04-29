#!usr/bin/python3

import my_pkg.binaryconversion

import my_pkg.intergers

while(1):
	n=int(input("Select menu: 1)conversion 2)union/intersection 3) exit ?"))
	if(n==1):
		my_pkg.binaryconversion.binconv()
	elif(n==2):
		my_pkg.intergers.integers()
	else:
		break

print("exit the program")
