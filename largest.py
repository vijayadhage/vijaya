mynum=[]
while True:
	inpt = raw_input("Enter a number: ")
	if inpt == "done" : break

	try:
        	num = int(inpt)
	except:
        	print "Invalid input"
		continue

	mynum.append(num)
	
	largest = max(mynum)
	smallest=min(mynum)


print "Maximum is", largest
print "Minimum is", smallest
