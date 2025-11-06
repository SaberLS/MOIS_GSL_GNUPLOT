#include <stdio.h>
#include <math.h>
#include <float.h>
#include <stdint.h>

// konwersje na zapis szesnastkowy
void double_to_hex(double val, char *out) {
    union {
        double d;
        uint64_t u;
    } conv;
    conv.d = val;
    sprintf(out, "0x%016llx", (unsigned long long)conv.u);
}

void float_to_hex(float val, char *out) {
    union {
        float f;
        uint32_t u;
    } conv;
    conv.f = val;
    sprintf(out, "0x%08x", conv.u);
}

int main(void) {


    // Nagłówek
    printf(
        "iteracja,"
        "float_mantysa_hex,"
        "double_mantysa_hex,"
        "float_exponent,double_exponent,"
        "float->double,"
        "float_hex,double_hex,float_as_double_hex\n");

    float f = 1.0f;
    double d = 1.0;
    int i = 0;
    int extra_iterations = 0;
    int float_denormal_found = 0, double_denormal_found = 0;

    while (1) {
        int ef, ed;
        double mf = frexp(f, &ef);
        double md = frexp(d, &ed);
        double fd = f; // float promowany do double

        char f_hex[16], d_hex[32], fd_hex[32];
        float_to_hex(f, f_hex);
        double_to_hex(d, d_hex);
        double_to_hex(fd, fd_hex);

        // mantysy w hex
        char mf_hex[32], md_hex[32];
        double_to_hex(mf, mf_hex);
        double_to_hex(md, md_hex);

        printf(
            "%d,%s,%s,%d,%d,%.15e,%s,%s,%s\n",
            i, mf_hex, md_hex, ef, ed, fd, f_hex, d_hex, fd_hex);

        // wykrycie liczb podnormalnych
        if (!float_denormal_found && fabsf(f) < FLT_MIN && f != 0.0f) {
            float_denormal_found = 1;
            extra_iterations = 4;
        }

        if (!double_denormal_found && fabs(d) < DBL_MIN && d != 0.0) {
            double_denormal_found = 1;
            if (extra_iterations < 4) extra_iterations = 4;
        }

        // zakończenie po +4 iteracjach po obu przejściach
        if (float_denormal_found && double_denormal_found) {
            if (extra_iterations == 0)
                break;
            extra_iterations--;
        }

        // kolejne dzielenie
        f /= 3.0f;
        d /= 3.0;
        i++;
    }

    return 0;
}
