"""Author:Annapoornima Koppad
	This programs checks if a number is prime or not
	Logic:
	If a number > 3, and is even, then it is not prime
	Otherwise
	if a number > 3 and is odd, I calculate the factorial of the number,
	and compare the factorial list with the list of the number itself,
	if these two lists are same, 
	then the number is prime, else it is not prime
	This logic does not consider 1 as a prime number
"""

#declare the primeflag to be false by default
primeFlag=False

#another program that I have writen returns the factorial of a number which is used by this program and hence it is imported here
from factorial import factorial

def checkprime(n, primeFlag):
	if n in (1,2,3):
		primeFlag=True
	else:
		#check if the number is even, if even set primeFlag to be false
		if n % 2 ==0:
			primeFlag=False
		else:
			#now number is no 1,2,3 and is odd.
			#calling the fatorial program and check if the factorial comprises of the number alone
			z=factorial(n)
			if z==[n]:
				#if true, set primeFlag to be true
				primeFlag=True
	return primeFlag

n=input("Enter the number that you want to check is prime: ")
print checkprime(n, primeFlag)

