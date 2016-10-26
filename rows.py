sam=[1,0,0,1,0,0,1,0,0]
row=[0,0,0]
col=[0,0,0]

k=0
#checking for rows
for i in (0,3,6):
	for j in range(3):
		if sam[i+j]==1:
			row[k]=1
			continue
		else:
			row[k]=0
			break
	k+=1

#checking for columns
s=0
for i in (0,1,2):
	for b in (0,3,6):
		if sam[i+b]==1:
			col[s]=1
			continue
		else:
			col[s]=0
			break
	s+=1

print "value of rows", row, col
