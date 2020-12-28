from math import sqrt 
from matplotlib import pyplot

#ex6
#1/
# a = [i/100 for i in range(0,1001,1)]
# print(a)

#explication de la composition de cette liste 
#je ne pouvais pas utilisé de float de 0.01 comme argument de pas pour aller de 0 à 10 
#donc j'ai divisé le i par 100 pour faire des pas de 0.01 et et mettre comme argument de pas 1
#et pour l'intervale de i j'ai mis une intervalle 0 -> 1001  
#car 1001/100 = 10.01 donc on revient à une intervalle de [0,10]


#2/
# x = [sqrt(i) for i in range(0,11)]
# print(x)


#3/
x = [i for i in range(0,11) ]
y = [sqrt(i) for i in range(0,11)]

pyplot.plot(x,y)
pyplot.show()