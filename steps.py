steps=input("Size: ")

for i in range(steps):
	j=steps-i-1
	print ' '*j+"/"+' '*(i*2)+'\\'
print '-'*(steps*2+1)

