import pandas as pd
import matplotlib.pyplot as plt
import struct
import numpy as np

# --- Funkcje pomocnicze do konwersji IEEE 754 z postaci szesnastkowej ---
def hex_na_float(h):
    """Konwertuj '0x...' (8 cyfr) na liczbę zmiennoprzecinkową 32-bit (float)."""
    try:
        if isinstance(h, str) and h.startswith("0x"):
            return struct.unpack('!f', bytes.fromhex(h[2:]))[0]
        return np.nan
    except Exception:
        return np.nan

def hex_na_double(h):
    """Konwertuj '0x...' (16 cyfr) na liczbę zmiennoprzecinkową 64-bit (double)."""
    try:
        if isinstance(h, str) and h.startswith("0x"):
            return struct.unpack('!d', bytes.fromhex(h[2:]))[0]
        return np.nan
    except Exception:
        return np.nan


# --- Wczytaj dane z pliku CSV ---
df = pd.read_csv("float_double_div3.csv")

# --- Konwersja mantys z postaci szesnastkowej na wartości liczbowe ---
df["float_mantysa_val"] = df["float_mantysa_hex"].apply(hex_na_double)
df["double_mantysa_val"] = df["double_mantysa_hex"].apply(hex_na_double)

# --- Konwersja rzeczywistych wartości float i double ---
df["float_val"] = df["float_hex"].apply(hex_na_float)
df["double_val"] = df["double_hex"].apply(hex_na_double)

# --- Oblicz różnicę między float i double ---
df["roznica"] = np.abs(df["double_val"] - df["float_val"])

# --- Kolumny do rysowania ---
iteracje = df["iteracja"]
float_exp = df["float_exponent"]
double_exp = df["double_exponent"]
float_val = df["float_val"]
double_val = df["double_val"]

# --- Granice normalizacji w IEEE754 ---
FLOAT_MIN_NORMAL = 2**-126
DOUBLE_MIN_NORMAL = 2**-1022

# --- Wykrycie momentu przejścia do liczb podnormalnych ---
float_podnormalny = np.argmax(float_val < FLOAT_MIN_NORMAL)
double_podnormalny = np.argmax(double_val < DOUBLE_MIN_NORMAL)

# Obsługa przypadku, gdy nie znaleziono (argmax zwraca 0 nawet jeśli warunek nigdy nie jest spełniony)
if float_val.iloc[float_podnormalny] >= FLOAT_MIN_NORMAL:
    float_podnormalny = None
if double_val.iloc[double_podnormalny] >= DOUBLE_MIN_NORMAL:
    double_podnormalny = None

# --- Tworzenie wykresów ---
plt.figure(figsize=(15, 12))

#  Cecha (exponent)
plt.subplot(4, 1, 1)
plt.plot(iteracje, float_exp, 'o-', label="float – cecha")
plt.plot(iteracje, double_exp, 'o-', label="double – cecha")
if float_podnormalny is not None:
    plt.axvline(x=float_podnormalny, color='red', linestyle='--', label='początek liczb podnormalnych (float)')
if double_podnormalny is not None:
    plt.axvline(x=double_podnormalny, color='orange', linestyle='--', label='początek liczb podnormalnych (double)')
plt.xlabel("Iteracja (kolejne dzielenie przez 3)")
plt.ylabel("Cecha (exponent)")
plt.title("Zmiana cechy dla float i double")
plt.legend()
plt.grid(True)

#  Mantysa
plt.subplot(4, 1, 2)
plt.plot(iteracje, df["float_mantysa_val"], 'o-', label="float – mantysa")
plt.plot(iteracje, df["double_mantysa_val"], 'o-', label="double – mantysa")
if float_podnormalny is not None:
    plt.axvline(x=float_podnormalny, color='red', linestyle='--')
if double_podnormalny is not None:
    plt.axvline(x=double_podnormalny, color='orange', linestyle='--')
plt.xlabel("Iteracja (kolejne dzielenie przez 3)")
plt.ylabel("Mantysa (wartość)")
plt.title("Zmiana mantysy dla float i double")
plt.legend()
plt.grid(True)

#  Wartość liczby
plt.subplot(4, 1, 3)
plt.plot(iteracje, float_val, 'o-', label="float – wartość")
plt.plot(iteracje, double_val, 'o-', label="double – wartość")
if float_podnormalny is not None:
    plt.axvline(x=float_podnormalny, color='red', linestyle='--')
if double_podnormalny is not None:
    plt.axvline(x=double_podnormalny, color='orange', linestyle='--')
plt.yscale('log')
plt.xlabel("Iteracja (kolejne dzielenie przez 3)")
plt.ylabel("Wartość (log)")
plt.title("Zmiana wartości float i double")
plt.legend()
plt.grid(True)

#  Różnica między float a double
plt.subplot(4, 1, 4)
plt.plot(iteracje, df["roznica"], 'o-', color='purple', label="|double - float|")
if float_podnormalny is not None:
    plt.axvline(x=float_podnormalny, color='red', linestyle='--', label='float – liczby podnormalne')
if double_podnormalny is not None:
    plt.axvline(x=double_podnormalny, color='orange', linestyle='--', label='double – liczby podnormalne')
plt.yscale('log')
plt.xlabel("Iteracja (kolejne dzielenie przez 3)")
plt.ylabel("Bezwzględna różnica (log)")
plt.title("Różnica pomiędzy wartościami double i float")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
