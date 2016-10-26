#Author:Annapoornima Koppad
#Date: 25 June 2016
#Purpose of Program: This program reads a file with lot of numbers and generates a list out of the file contents and prints the list

f=open('sample.txt','r')
y=[]
for a in f:
	b=a.split()
	for c in b:
		if c[0]=='[':
			d=c[1:]
		elif c[-1]==']':
			d=c[:-1]
		else:
			d=c
		y.append(d)
f.close()
print y
