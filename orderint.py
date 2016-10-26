"""This program takes in three integers and returns True if they are in ascending order"""

def orderInt():
        print "Enter 3 integers: "
        a = input()
        b = input()
        c = input()
        if a<b<c:
            return True
        else:
            return False

print orderInt()


def orderInt1(a,b,c):
	print "Enter 3 integers: "
        if a<b<c:
            return True
        else:
            return False

a = input('1')
b = input('2')
c = input('3')
    
print orderInt1(a,b,c)
