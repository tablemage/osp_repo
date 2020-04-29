#!/usr/bin/python3

import re

def integers():
	listring1=(input("1st list: "))
	listring2=(input("2nd list: "))

	list1=re.findall("\d+",listring1)
	list2=re.findall("\d+",listring2)
	list1.sort()
	list2.sort()
	intersect=list(set(list1)&set(list2))
	union=list(set(list1)|set(list2))
	union=[int (i) for i in union]
	intersect=[int (i) for i in intersect]
	union.sort()
	intersect.sort()
	print("=> union ", end="")
	print(union)
	print("=> intersection ", end="")
	print(intersect)
