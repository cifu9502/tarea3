# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import string
infile = open('Notas.csv', 'r')

#load the full text by lines
text = infile.readlines()
arch = open('notas.dat', 'w')
a = 0
C = text
#lee cada linea y cambia las comas por + 
for x in text:
    arch.write(x.replace(",", "+"))    
arch.close()    

# <codecell>

#Hace lo mismo que el otro pero en bash
!cat Notas.csv | sed 's\,\+\' > notas2.dat

# <codecell>


