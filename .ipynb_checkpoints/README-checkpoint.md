# Kodilla_m07
7th module tasks

### Zadanie 7.1
Ćwiczenie: tworzę notatnik<br>

Skoro potrafisz już stworzyć notatnik i znasz podstawy Pythona, możesz zaprezentować swoje możliwości w następujący sposób. Stwórz kolejny o nazwie functions i umieść w nim 4 komórki. Wyobraź sobie, że chcesz zaprezentować swojemu koledze jak prosto stworzyć funkcje w Pythonie i z nich korzystać.<br>
W komórce typu Markdown opiszesz, jak tworzymy funkcję, np. "używamy słowa def" itd. Potem napisz komórkę z kodem, która taką funkcję stworzy, np. dodawanie dwóch liczb. Kolejna komórka typu Markdown ma krótko opisać jak wywołujemy funkcję (np. że używamy nawiasów okrągłych). Następnie, w ostatniej komórce, pokaż przykład wywołania tej prostej funkcji.<br>
Magiczne komendy z IPython mają zastosowanie też w Jupyterze.<br>


### Zadanie 7.4
Ćwiczenia<br>
<prep>
    Stwórz dziesięcioelementowy wektor z przedziału od 0 do 1, bez uwzględniania wartości granicznych.
    Stwórz macierz o wymiarach 5x5, której wartości w poszczególnych wierszach są równe, a wartości w kolumnach wynoszą 0, 1, 2, 3, 4.
</prep>


### Zadanie 7.5.1
Ćwiczenie<br>
Znajdź indeksy niezerowych elementów z tablicy array([1,2,0,0,4,0]).<br>


### Zadanie 7.5.2
Ćwiczenia<br>
<prep>
    Wyfiltruj z arr tylko te wartości, które są mniejsze od 10 lub większe bądź równe 20, ale jednocześnie różne od liczby 40. (gdzie arr = np.arange(0,50,5)).
    Wykorzystując operator XOR, stwórz macierz o kształcie (4,4), której elementy po głównej przekątnej mają wartość logiczną False, a pozostałe wartość True.
</prep>


### Zadanie 7.5.3
Ćwiczenie<br>
<prep>
    Zwróć z macierzy arr wiersz o indeksie nr 2, lecz tylko dla tych kolumn, których suma przekracza 30.
    Mamy dane dwie tablice: a i b. Stwórz program filtrujący wartości z b, które korespondują z elementami a i są większe od 100 i mniejsze od 110.

a = np.array([97,101,105,111,117,125])
b = np.array(['a','e','i','o','u','y'])

    Stwórz program, który ze wskazanej macierzy wyciągnie odpowiednio najmniejszą i największą wartość dla każdego wiersza.

[[0 4 1]
[2 0 4]]

    Mając tablicę np.arange(11), odwróć znak wszystkich elementów większych od 3 i mniejszych od 8.
</prep>


### Zadanie 7.5.4
Ćwiczenia<br>
<prep>
    Stwórz program, który ze wskazanej macierzy wyciągnie odpowiednio najmniejszą i największą wartość dla każdego wiersza.

    [[0 4 1]
    [2 0 4]]

    Stwórz wektor Z według następującego wzoru: np.random.uniform(0,1,10). Następnie znajdź element, który jest najbliższy wartości 0.5.
    Stwórz wektor zawierający 20 losowych wartości, a następnie zamień jego największą wartość na 0.
    Znajdź części całkowite tablicy, wykorzystując przynajmniej dwa różne sposoby.

np.array([5, 0.0249139 , 0.11873564, 0., 0.72321586, 11308494, 0.29931472, 0.24439968, 0.61251754, 4])
</prep>


### Zadanie 7.5.5
Ćwiczenie<br>
Posortuj wektor arr w sposób malejący, biorąc pod uwagę wyniki z drugiego egzaminu.<br>


### Zadanie 7.5.6
Zadanie: kupujemy mieszkanie<br>
Zamierzasz kupić mieszkanie. Upatrzone M kosztuje w tym momencie 120 tys. zł, jednak przewidujesz, że przez następne 5 lat ceny mieszkań będą rosły w tempie 5% rocznie. W tym momencie nie dysponujesz wystarczającymi środkami, dlatego znajdujesz ofertę banku, który proponuje lokatę, do której dopłacasz pewna stałą kwotę na koniec każdego miesiąca. Bank oferuje nominalną stopę procentową w wysokości 12% w skali roku, przy kapitalizacji miesięcznej.<br>
<prep>
    Ile będzie wynosiła orientacyjna cena mieszkania za 5 lat?
    Ile musisz wpłacać do banku każdego miesiąca, aby przy przedstawionej ofercie uzbierać na mieszkanie w ciągu 5 lat?
    Stwórz wykres przedstawiający, jak w interwałach miesięcznych zmieniać się będzie cena mieszkania (liniowy wzrost w całym okresie) oraz wartość twojej lokaty.
</prep>
Do wykonania powyższego zadania wykorzystaj biblioteki NumPy, NumPy-financial oraz Matplotlib. Odpowiedzi na pytania umieść w Notebooku (jeśli korzystasz) lub w komentarzach w kodzie.<br>