a=[1,2,3,4,5,6,7,8,9]
print a

i=0
while i<9:
	if a[i]=='*':
		i+=4
		if a[i]=='*':
			i+=4
			if a[i]=='*':
				setleftdiagonal=True
	i=2
	if a[i]=='*':
		i+=2
		if a[i]=='*':
			i+=4
			if a[i]=='*':
				setrightdiagonal=True
				i=9

print "Out of loop", setleftdiagonal, serightdiagonal



