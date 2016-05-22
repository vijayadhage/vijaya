'''Author: Annapoornima Koppad
Date: 22-May-2016
This program sums the diagonals'''

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
m=n-1
sum1,sum2=0,0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][m-i]
    
print abs(abs(sum1)-abs(sum2))
