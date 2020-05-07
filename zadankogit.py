def ostatni_element(lista):
    return lista[-1] # it returns the last element from list, which will be given below

wyraz = input("Wpisz losowy wyraz, by utworzyć z niego listę: ") # allows to create your own list
lista = list(wyraz) # shows created list
wynik = ostatni_element(lista)
print(wynik)
