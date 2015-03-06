# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#El resultado es el n-esimo numero de fibbonacci. Si queremos subir una escalera de n piezas hay dos posibilidades 
#para el primer paso. Si se da un solo paso, terminar de subir es simplemente el caso n-1, mientras que si se dan dos 
# pasos al inicio, terminar de subir es el caso n-2. De cualquier forma, el numero de formas de subir una escalera de n 
#piezas es el numero de formas de subir una de n-1 piezas + el numero de formas de subir una de n-2. Los casos bases son 
# n=1  hay 1 forma y n = 2 hay dos formas. Esto nos da la recurrencia de fibbonacci por lo que basta con calcularla

def calcularFib(n):
    n1 = 1
    n2 = 2
    i = 2
    while(i<n):
        n2 = n1+n2
        n1 = n2-n1
        i = i+1
       
    return n2
        
print "Para una escalera de 13 la respuesta es %d" % calcularFib(13)
print "Para una escalera de 15 la respuesta es %d" % calcularFib(15)

# <codecell>

import numpy as np

# <codecell>

#b.
import numpy as np
#tomamos estas matrices como ejemplo
A = [4,4,5,5,1]
B = [3,2,4,3,1]

#Las matrices A y B tienen que ser de tamaños iguales, de lo contrario el codigo no va a funcionar
def escalera(A,B):
    L = len(A)
    C = np.zeros(L)
    for x in range(0,L):
        C[x] = (calcularFib(A[x]))%(2*B[x])
    return C
    
        
    

# <codecell>


escalera(A,B)

# <codecell>

#Otro ejemplo
A = [4,4,5,5,1, 6,7,7,9]
B = [3,2,4,3,1, 6,3,2,9]
escalera(A,B)

# <codecell>


