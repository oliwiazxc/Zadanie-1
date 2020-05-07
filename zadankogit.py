import random
def ostatni(listaLiczb):
    print('[*] lista w rekurencji = ', listaLiczb)
    if len(listaLiczb) == 1:
        return listaLiczb[0]
    else:
        return ostatni(listaLiczb[1:])

for i in range(3):
    lista=[]
    for i in range(7):
        lista.append(random.randint(1,100))
    print('lista= ', lista)
    print('ostatni element = ', ostatni(lista))
    print()
print("mogę edytować tylko mastera noo:((")
