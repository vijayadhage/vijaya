"""	Author:Annapoornima Koppad
	Purpose: This program calculates the factorials of a given number
"""

#define an empty list to store the factorials
x=[]

#function to calculate factorials
def factorial(n):
	i=n
	""" To optimize, I have used the folllowing technique,
	I check if the remainder of values that range from 2 to half the number value is zero
	if its zero, then 
	"""
	for j in range(2,((i/2)+1)):
		if i % j == 0:
			x.append(j)
	x.append(n)
	return x

print "here"
