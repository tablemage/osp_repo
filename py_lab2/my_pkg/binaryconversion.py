#!/usr/bin/python3

def binconv():
	data=int(input("input binary number: "), 2)
	octdata=format(data,'o')
	hexdata=format(data,'x')
	print("OCT> ", end="")
	print(octdata)
	print("DEC> ", end="")
	print(data)
	print("HEX> ", end="")
	print(hexdata)
