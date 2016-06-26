#! /usr/bin/python python
import datetime
import random
import matplotlib.pyplot as plt
from time import sleep


#x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
#y = [i+random.gauss(0,1) for i,_ in enumerate(x)]
fig=plt.figure()
plt.title("Continous temperature data display")
plt.xlabel("Time")
plt.ylabel("Temperature")
ax=fig.add_subplot(111)
x=[datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
labels=x
y=[i+random.gauss(0,1) for i,_ in enumerate(x)]

li, = ax.plot(x,y)
plt.xticks(x,labels, rotation='vertical')
plt.show(block=False)

fig.canvas.draw()

while True:
        y[:-10]=y[10:]
	x[:-10]=x[10:]
	labels[:-10]=labels[10:]
	x=[datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
	labels=x
	y=[i+random.gauss(0,1) for i,_ in enumerate(x)]
	plt.xticks(x,labels, rotation='vertical')
	plt.show(block=False)

	li.set_ydata(y)
	fig.canvas.draw()
	sleep(5)	
