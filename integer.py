""" Author: Annapoornima Koppad
    If is odd, print Weird
    If is even and in the inclusive range of to , print Not Weird
    If is even and in the inclusive range of to , print Weird
    If is even and greater than , print Not Weird
"""

n=int(raw_input("Enter the integer"))
if n % 2 == 1:
	print "Weird"
else:
	if  n in (2,4,6):
		print "Not Weird"
	elif n in range(6,21):
		print "Weird"
	else:
		print "Not Weird"
