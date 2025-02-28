import numpy as np

# Tworzenie tablicy
array = np.array([1, 2, 0, 0, 4, 0])

# Znajdowanie indeksów niezerowych elementów
indeksy_niezerowych = np.nonzero(array)

print("Indeksy niezerowych elementów:")
print(indeksy_niezerowych)

# Sprawdź, które środowisko Python jest używane w VSCode
#     Otwórz VSCode.
#     Otwórz plik Pythona (np. Task_7.5.1.py).
#     Kliknij na dolnym pasku statusu (na dole okna VSCode) w sekcję, która pokazuje aktualnie wybrany interpreter Pythona. Może to wyglądać np. tak: Python 3.9.7 lub Python 3.8.10.
#     Zostanie wyświetlona lista dostępnych interpreterów. Wybierz ten, w którym zainstalowałeś numpy (ten sam, który działa w Jupyterze).