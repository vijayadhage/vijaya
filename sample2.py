import os

filepath = os.getcwd()
backslash = "\\"
allfiles = os.listdir(filepath)
filelist=len(allfiles)
i,j=0,0
dirdir, filedir=[], []
for indexval in range(filelist):
   #print "File  ", indexval, allfiles[indexval], type(allfiles[indexval])           
   checkfileisdir = filepath + backslash + allfiles[indexval]
   if os.path.isdir(checkfileisdir):
       print "directory no ", i, " ",allfiles[indexval]
       dirdir.append(checkfileisdir)
       i+=1
   else:
       print "file no ", j, " ", allfiles[indexval]
       j+=1
       filedir.append(checkfileisdir)
pickfilechoice=input("Enter your directory choice in numbers and the file to move :")

print "moving {0} file to  {1}",(pickfilechoice)

# to do the same thig as above with map function

pathstr=filepath + backslash
print allfiles, pathstr
#print map(pathstr+=allfiles, allfiles)

