# Wstęp do biblioteki GSL oraz narzędzia GNUPLOT

## 📘 Opis projektu

Projekt stanowi rozwiązanie zadań laboratoryjnych z tematu **Arytmetyka
komputerowa**, realizowanych w ramach kursu **Metody obliczeniowe i symulacje**.
Celem ćwiczenia jest praktyczne zbadanie możliwości biblioteki GSL i narzędzia
graficznego Gnuplot oraz jak możemy te możliwości wykorzystać do celów
realizacji laboratoriów.

---

## ⚠️ Źródło zadań

Zadania, do których odnoszą się rozwiązania w tym repozytorium, pochodzą z
materiałów dydaktycznych których autorem jest dr. Włodzimierz Funika
udostępnionych w ramach kursu _Metody obliczeniowe i symulacja_
[WSZiB](https://www.wszib.edu.pl/).

Oryginalna treść zadań dostępna jest pod adresem:
[https://artemis.wszib.edu.pl/~funika/mois/lab2/](https://artemis.wszib.edu.pl/~funika/mois/lab2/)

Autor niniejszego repozytorium **nie jest autorem zadań**, a jedynie autorem
**rozwiązań i opracowania kodu źródłowego**.

---

## 🧮 Zakres zadań

1.  [ ] **Zadanie - dokładność**

    Potrzebne pliki
    [Wzorcowy Makefile](https://artemis.wszib.edu.pl/~funika/mois/lab2/Makefile)
    [dokladnosc.c](https://artemis.wszib.edu.pl/~funika/mois/lab2/dokladnosc.c)
    skompilować program `dokladnosc.c` przy użyciu polecenia make, a następnie
    uruchomić go. Korzystając z funkcji gsl_ieee_printf_double zobaczyć, jak
    zmienia się mantysa i cecha dla coraz mniejszych liczb. Kiedy mantysa nie
    jest w postaci znormalizowanej?

---

2. [ ] **Zadanie - gnuplot**

   Prosze odtworzyc wykres znajdujacy sie na
   [rysunku](https://artemis.wszib.edu.pl/~funika/mois/lab2/testowy.png) Przy
   pomocy gnuplot prosze narysowac dane zgromadzone w pliku
   [dane1.dat](https://artemis.wszib.edu.pl/~funika/mois/lab2/dane1.dat). Aby
   wykres byl czytelny, jedna z osi musi miec skale logarytmiczna. Prosze
   ustalic, ktora to os i narysowac wykres. Prosze narysowac wykres funkcji
   dwywymiarowej, ktorej punkty znajduja sie w pliku
   [dane2.dat](https://artemis.wszib.edu.pl/~funika/mois/lab2/dane2.dat). Prosze
   przegladnac plik i sprobowac znalezc w nim maksimum. Potem prosze
   zlokalizowac maksimum wizualnie na wykresie. Prosze na wykresie zaznaczyc
   maksimum jako notke (np. set arrow).

---

[ ] **3. Sporządzenie sprawozdania** Na podstawie wykonanych zadań należy opracować
sprawozdanie zawierające pełną analizę wyników i wniosków.

### Wymagania dotyczące sprawozdania:

**Nagłówek:**

- [ ] numer laboratorium
- [ ] temat
- [ ] autor
- [ ] data

**Zawartość:**

- [ ] Treść zadania
- [ ] Moje podejście do rozwiązania problemu — jak najgłębsza argumentacja
      przyjętego podejścia
- [ ] Ważniejsze fragmenty kodu
- [ ] Wyniki (liczby, wykresy, tabele)
- [ ] Wnioski (związki przyczynowo-skutkowe)
- [ ] Bibliografia
