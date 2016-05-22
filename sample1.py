import os

filepath = os.getcwd()
backslash = "\\"
allfiles = os.listdir(filepath)
filelist=len(allfiles)

for indexval in range(filelist):
   print "File  ", indexval, allfiles[indexval], type(allfiles[indexval])   
checkfileisdir = filepath + backslash
dirsavailable = [checkfileisdir + indexval for indexval in allfiles]
for checkfile in dirsavailable:
    print os.path.isdir(checkfileisdir)
