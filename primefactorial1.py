"""Hacker Rank problem: """
"""This tehnique uses memory optimization"""
"""This program returns the unique prime factors of a number"""

factorialist={}

def factorial3(n):
	if n not in factorialist:
	        x=[j for j in range(1, ((n/2)+1)) if n%j==0]
        	x.append(n)
		factorialist[n]=x
	return factorialist[n]


n=input()
numbers=[]
for i in range(n):
	numbers.append(input())

count=[0 for j in numbers]
for i,k in enumerate(numbers):
	for j in factorial3(k):
		if factorial3(j)==[1,j]:
			count[i]+=1

print "first crude attempt here", zip(numbers, count)
#c=[0 for i in numbers]
#unique_dict={}
#for i in numbers:
#	unique_dict[i]=0
#new2=[unique_dict[k]+1 for i,k in enumerate(numbers) for j in factorial3(k) if factorial3(j)==[1,j]]
#print new2, "here"

oldnumbers=numbers
oneFlag=False
if 1 in numbers:
	oneFlag=True
	numbers=[i for i in oldnumbers if i!=1]

new1=[i+1 for i,k in enumerate(numbers) for j in factorial3(k) if factorial3(j)==[1,j]]

c1={}
for i in new1:
	if i not in c1:
		c1[i]=1
	else:
		c1[i]+=1

#sortedcount=[(k,v) for k,v in sorted(c1.items(), key = lambda x: x[0])]
#sortedcountno=[v for k,v in sortedcount]
sortedc=[v for k,v in sorted(c1.items(), key=lambda x:x[0])]
x=zip(numbers, sortedc)

if oneFlag:
	x.append((1,0))

print x

#print zip(numbers, c1.values())

#new1=[c[i]+1 for i,k in enumerate(numbers) for j in factorial3(k) if factorial3(j)==[1,j]]
#new3=[1 for i,k in enumerate(numbers) for j in factorial3(k) if factorial3(j)==[1,j]]
#print new3





