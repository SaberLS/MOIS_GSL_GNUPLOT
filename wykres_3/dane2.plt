reset

set terminal pngcairo
set output "wykres.png"

set title "Powierzchnia funkcji z pliku dane2.dat"
set xlabel "x"
set ylabel "y"
set zlabel "z"
set grid
set hidden3d

# policz statystyki kolumny z (3)
# stats "dane2.dat" using 3

# maksimum
xmax = 4
ymax = 3
zmax = 1

# Zaznaczenie maksimum
set label sprintf("Maksimum (%.2f, %.2f, %.2g)", xmax, ymax, zmax) at xmax, ymax, zmax offset 1,1
set arrow from xmax, ymax, zmax+0.0001 to xmax, ymax, zmax lw 2 lc rgb "red" head filled

# Rysowanie wykresu 3D
splot "dane2.dat" using 1:2:3 with lines title "f(x,y)"
