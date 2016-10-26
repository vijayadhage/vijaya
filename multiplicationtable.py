print "**This program prints the multiplication table upto 10 for the number that you enter**"
n=input("Enter the number who's multiplication table you want printed")
print "**Printing multipication table for %d**" %(n)

for i in range(1,11):
	print str(n) +" * "+str(i)+" = "+str(n*i)
print "End of table"
