A=[5,8,14,46]

f=open('new.txt', 'a')
f.write(str(A))
f.close()

f=open('new.txt', 'r')
for i in f.readline():
	print i
