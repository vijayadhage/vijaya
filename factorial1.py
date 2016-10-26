
x=[]
def checkprime(n):
	i=n
	for j in range(2,((i/2)+1)):
		if i % j != 0:
			continue
		else:
			x.append(j)
	x.append(n)
	return
n=input("Enter the number you want to check is prime: ")
checkprime(n)
print x



