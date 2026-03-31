#include <stdio.h>

int main() {
    printf("Tamanho de int: %zu bytes\n", sizeof(int));
    printf("Tamanho de float: %zu bytes\n", sizeof(float));
    printf("Tamanho de double: %zu bytes\n", sizeof(double));
    printf("Tamanho de char: %zu bytes\n", sizeof(char));
    printf("Tamanho de long long: %zu bytes\n", sizeof(long long));

    return 0;
}