largest=None
smallest=None
while True:
	inpt = raw_input("Enter a number: ")
	if inpt == "done" : break

	try:
        	num = int(inpt)
	except:
        	print "Invalid input"
		continue

	if largest is None:
		largest=num
	elif num>largest:
		largest=num

	if smallest is None:
		smallest=num
	elif num<smallest:
		smallest=num


print "Maximum is new here", largest
print "Minimum is", smallest
