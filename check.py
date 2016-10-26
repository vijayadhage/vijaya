# this programs checks the values of matrix to see if thery are filled

sam=['*','*','*','*','*',0,'*','*',0]
userdata=[0 for k in range(8)]

#check if any of the rows are filled by the user
#rows are [0,1,2], [3,4,5],[6,7,8]
k=0
for i in range(3): # for three rows
	j=0 
	while j<3:	
		if sam[k]=='*':
			userdata[i]+=1
		k+=1
		j+=1

print userdata, k

k=0
for i in range(3,6): #no of columns
	j=0
	while j<3:
		if sam[k]=='*':
			userdata[i]+=1
		k+=3
		j+=1
	k=k-8

print userdata


for j in range(0,9,4):
	if sam[j]=='*':
		userdata[6]+=1

print userdata

for j in range(2,7,2):
	if sam[j]=='*':
		userdata[7]+=1

print userdata
		
	
		

#check if any of the columns are filled by the user
#columns are [0,3,6],[1,4,7],[2,5,8]

#check if  any of the diagonals are filled by the user
#diagonals are [0,4,8],and [2,4,6]

#of the above three choices, choose the one location that the user will not win and the computer wins
