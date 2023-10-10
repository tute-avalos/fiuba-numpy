'''
Un poco más sobre variables y especialmente listas...
'''

LISTA = [ i*2 for i in range(10) ]
print("Lista completa:", LISTA)

sublista = LISTA[:5]
print("Sublista LISTA[:5] ->", sublista)

sublista = LISTA[5:]
print("Sublista LISTA[5:] ->", sublista)
