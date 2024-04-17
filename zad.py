def oblicz_srednia_ocen(oceny):
    suma_ocen = sum(oceny)
    liczba_ocen = len(oceny)
    srednia = suma_ocen / liczba_ocen
    return srednia

def sortuj_liste(lista, rosnaco=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if rosnaco:
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def suma_dwoch_list(lista1, lista2):
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma

def odwroc_liste(lista):
    odwrocona = []
    for i in range(len(lista)-1, -1, -1):
        odwrocona.append(lista[i])
    return odwrocona

def main():
    while True:
        print("\nMenu:")
        print("1. Oblicz średnią ocen")
        print("2. Sortuj listę liczb")
        print("3. Suma dwóch list")
        print("4. Odwróć kolejność elementów w liście")
        print("5. Wyjdź z programu")
        
        wybor = input("Wybierz opcję (1/2/3/4/5): ")
        
        if wybor == '1':
            oceny = [int(x) for x in input("Podaj oceny oddzielone spacją: ").split()]
            print("Średnia ocen:", oblicz_srednia_ocen(oceny))
        elif wybor == '2':
            liczby = [int(x) for x in input("Podaj liczby oddzielone spacją: ").split()]
            kolejnosc = input("Sortować rosnąco (tak/nie): ")
            rosnaco = True if kolejnosc.lower() == 'tak' else False
            print("Posortowana lista:", sortuj_liste(liczby, rosnaco))
        elif wybor == '3':
            lista1 = [int(x) for x in input("Podaj pierwszą listę liczb oddzielone spacją: ").split()]
            lista2 = [int(x) for x in input("Podaj drugą listę liczb oddzielone spacją: ").split()]
            print("Suma dwóch list:", suma_dwoch_list(lista1, lista2))
        elif wybor == '4':
            lista = [int(x) for x in input("Podaj listę liczb oddzielone spacją: ").split()]
            print("Odwrócona lista:", odwroc_liste(lista))
        elif wybor == '5':
            print("Koniec programu.")
            break
        else:
            print("Niepoprawny wybór. Wybierz opcję od 1 do 5.")

if __name__ == "__main__":
    main()
