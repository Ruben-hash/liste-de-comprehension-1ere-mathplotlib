from math import sqrt 
from matplotlib import pyplot

#ex6
#1/
# a = [i/100 for i in range(0,1001,1)]
# print(a)

#2/
# x = [sqrt(i) for i in range(0,11)]
# print(x)


#3/
x = [i for i in range(0,11) ]
y = [sqrt(i) for i in range(0,11)]

pyplot.plot(x,y)
pyplot.show()
