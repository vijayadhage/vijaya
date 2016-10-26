import sys, os

def getfiles(currdir):
    myfiles = []
    currdir=os.listdir(os.getcwd())
    for file in currdir:
         for file in currdir:
            path = os.path.join(currdir,file)
            if not os.path.isdir(path):
                myfiles.append(path)
            else:
                getfiles(path)
    return(myfiles)

if __name__ == '__main__':
    filedirectory = []
    filedirectory = getfiles(sys.argv[1])
    print(filedirectory)
