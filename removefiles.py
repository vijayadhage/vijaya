# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:59:10 2016

@author: Annakoppad
"""

import os

filepath=os.getcwd()
backslash="\\"
allfiles=os.listdir(filepath)

filechoicestr="What do you want to do now? \n \
    press d for displaying all files in directory! \n \
    press r for removing files in the directory! \n \
    press m to move the files to another directory \n \
    please provide your input :"

filechoice=input(filechoicestr)

filelist=len(allfiles)

if filechoice=='d':
    for indexval in range(filelist):
        print "File no ",indexval, allfiles[indexval]
elif filechoice=='r':
    print "These are the files available for deleting!"
    for indexval in range(filelist):
        print "File  ",indexval, allfiles[indexval]
    filenum=input("Enter your file number to delete")
    selectfile=allfiles[filenum]
    querystring= "do you want to delete this file " + selectfile + " say y or yes :"
    choice=input(querystring)
    if choice == 'y' or choice=='yes':
        os.remove(filepath+backslash+selectfile)
elif filechoice=='m':
    for indexval in range(filelist):
       print "File  ",indexval, allfiles[indexval], type(allfiles[indexval])           
       checkfileisdir=filepath+backslash+allfiles[indexval]
    #    diravailable=[filepath+backslash+allfiles[indexval] for indexval in allfiles] 
       print os.path.isdir(checkfileisdir), "new"
   # print dirsavailable

print "Exiting the program"