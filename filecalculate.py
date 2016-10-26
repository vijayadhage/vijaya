fname=raw_input("Enter the file name:")
readf=open(fname)
l=0.0
a=0.0
for line in readf:
	if line.startswith('X-DSPAM-Confidence'):
		l+=1
		pos=line.strip().find(':')
		value=line[pos+1:pos+8]
		a+=float(value.strip())

print "Average X-DSPAM-Confidence is :"+str(a/l)+"lines="+str(l)
	
