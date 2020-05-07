def ostatni_element(lista):
    return lista[-1] # zwróć ostatni element z tej listy, która zostanie podana niżej

wyraz = input("Wpisz losowy wyraz, by utworzyć z niego listę: ")
lista = list(wyraz)
wynik = ostatni_element(lista)
print(wynik)
