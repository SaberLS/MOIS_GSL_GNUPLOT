set terminal pngcairo
set output "wykres.png"

set title "Wykres danych z pliku dane1.dat"
set xlabel "x"
set ylabel "y"

# Ustawienie osi X w skali logarytmicznej
set logscale x

# Dodanie siatki dla czytelności
set grid

# Ustawienie stylu linii i punktów
set style line 1 lt 1 lw 3 pt 7 ps 1.0 lc rgb "blue"  # pt 5 = kwadraty, ps 1.0 = mniejsze punkty

# Rysowanie wykresu z linią i punktami ze stylem linii 1
plot "dane1.dat" using 1:2 with linespoints ls 1 title "Dane z dane1.dat"

pause -1
