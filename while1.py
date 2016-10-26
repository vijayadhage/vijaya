def check_status():
	choice=raw_input("Enter you choice")
	return choice

def function():

	while True:
        	c=check_status() #External function that returns a new status value if it changes
        	print c

	        if c == "yes":
        		print "enter", c
			continue
	        elif c == '1':
			print "no", c
			continue
		else:
			break

function()
