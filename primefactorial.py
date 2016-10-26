"""This program calculates the factorial of prime numbers and prints if the number is prime or not"""
""" This program considers 1 as a non prime number"""

def factorial1(n):
	x=[i for i in range(1,((n/2)+1)) if n%i ==0]
	x.append(n)
	return x

def checkprime1(n):
	return factorial1(n)==[1,n] 


print checkprime1(input())
