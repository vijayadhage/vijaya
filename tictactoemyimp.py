''' Tic Tac toe game
Author: Annapoornima Koppad
Date:17-May-2016'''


    
def printtictactoe(val=0):
    print "\t****Tic Tac Toe****"
    print "\t-------------------"
    i=0
    while i<9:
        print "\t|  %d,%d  |  %d,%d  |  %d,%d  |" %(val,i,val,i+=1,val,i+=1)
        print "\t-------------------"
        print "\t|  %d,%d  |  %d,%d  |  %d,%d  |" %(val,i,val,i+=1,val,i+=1)
        print "\t-------------------"
        print "\t|  %d,%d  |  %d,%d  |  %d,%d  |" %(val,i,val,i+=1,val,i+=1)
        print "\t-------------------"
        return

firstplayer=input("Enter 1 if you want to play first : ")
inputcoordinates=input("Enter the cordinates where you want mark separated by a , : ")
if firstplayer==1:
    print firstplayer, "here"
    printtictactoe()
