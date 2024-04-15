if __name__ == '__main__':

    while True:
        print('Wybierz opcję:')
        print('1. Obliczanie średniej arytmetycznej')
        print('2. Podnieś liczbę do potęgi')
        print('3. Porównaj ze sobą dwie liczby')
        print('4. Wyjdź')

        wybór = int(input('Wybierz opcję: '))

        if wybór == 1:
            liczba1 = float(input('Liczba 1: '))
            liczba2 = float(input('Liczba 2: '))
            średnia = (liczba1 + liczba2) /2
            print(f'Średnia arytmetyczna wynosi {średnia}')
        elif wybór == 2:
            podstawa = float(input('Podstawa: '))
            wykładnk = float(input('Wykładnik: '))
            wynik = podstawa ** wykładnk
            print(f'{podstawa} do {wykładnk} wynosi {wynik}')
        elif wybór == 3:
            liczba1 = float(input('Liczba 1: '))
            liczba2 = float(input('Liczba 2: '))
            if liczba1 > liczba2:
                większa = liczba1
            else:
                liczba1 < liczba2
                większa = liczba2
            print(f'Większa liczba to {większa}')
        elif wybór == 4:
            break


