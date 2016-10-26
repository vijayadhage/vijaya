#This program solves for simultaneous equations in two variables x,y
#It takes four inputs from user, and two outputs from user and provides values for x , and y

#prompt the user to provide coefficients of the first and second equation, their outputs
firsteq=map(int,raw_input("Enter the two coefficiecients of x, and y, the output : ").split())
secondeq=map(int,raw_input("Enter the two coefficiecients of x, and y, and the output : ").split())

print firsteq, secondeq

#the solution to the matrix is as follows, sol = A**(-1) * B 
#where A is the matrix of coeficient and B is the solution 

for i in range(2):
	for i in range(3):
		




