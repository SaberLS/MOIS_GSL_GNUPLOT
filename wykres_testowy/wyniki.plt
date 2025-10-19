# Ustawienie terminala graficznego — tutaj PNG z silnikiem Cairo
# "enhanced" pozwala na formatowanie tekstu (indeksy, greckie litery itp.)
set terminal pngcairo size 799,571

# Ustawienie nazwy pliku wyjściowego, do którego zostanie zapisany wykres
set output "wykres.png"

# Konfiguracja legendy (klucza):
# - fixed: pozycja statyczna
# - left top: w lewym górnym rogu
# - vertical: elementy w kolumnie
# - Right: tekst legendy po prawej stronie symbolu
# - noreverse: zachowuje kolejność rysowania
# - enhanced: pozwala na formatowanie tekstu
# - autotitle: automatycznie używa tytułów serii danych
# - box lt black linewidth 1 dashtype solid: ramka wokół legendy
set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1 dashtype solid

# Tytuł wykresu
set title "Wykres testowy"

# Dodatkowe ustawienia tytułu:
# - textcolor lt -1 → domyślny kolor (czarny)
# - norotate → tekst poziomy
set title textcolor lt -1 norotate

# Opisy osi
set xlabel "x"
set ylabel "Amplituda"

# Zakres osi X i Y
set xrange [-3:3]
set yrange [-4:5]

# Definicja stylu linii dla siatki (gridu)
# dashtype (2,30): linia przerywana (2 px kreska, 30 px przerwa)
# lt rgb "black": kolor czrny
# lw 1: grubość linii
set style line 11 dashtype (2,30) lt rgb "black" lw 1

# Włączenie siatki z użyciem stylu 11
set grid ls 11

# Grubość obramowania wykresu (np. osi)
set border lw 2

# Domyślny styl danych: linie
set style data lines

# Szerokość prostokątów przy rysowaniu z 'with boxes'
# "1 relative" oznacza, że szerokość = 100% odstępu między punktami
set boxwidth 1 relative

# --- Rysowanie wykresu ---
# Plik "fun1.txt" zawiera kolumny: x, y, błąd
# using 1:($2+$3)/2:2:3 → średnia, y, yerror (sposób przetwarzania danych)
# w yerrorbars → rysuje punkty z paskami błędów
# lt rgb "red" → kolor czerwony
# lw 2 → grubość linii 2
# Kolejne funkcje rysowane są z innymi kolorami i stylami
plot "fun1.txt" using 1:($2+$3)/2:2:3 w yerrorbars lt rgb "red" lw 2 title "Dane z pliku fun1.txt", \
     sin(x**5) title "funkcja2: sinus(x^5)" lw 2 lt rgb "green", \
     2*cos(x*sin(x)) title "funkcja1: 2*cos(x*sin(x))" lw 1 lt rgb "blue" with boxes, \
     3*sin(x) title "funkcja3: 3*sin(x)" lw 2 lt rgb "red"
