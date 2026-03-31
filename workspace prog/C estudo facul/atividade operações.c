#include <stdio.h>

int main() {
    int n1, n2;
   printf("digite um numero inteiro:");
    scanf("%d",&n1);

    printf("digite outro valor inteiro:");
    scanf("%d",&n2);


    printf("Soma: %d\n", n1 + n2); 
    printf("Subtracao: %d\n", n1 - n2); 
    printf("Multiplicacao: %d\n", n1 * n2); 
    printf("Divisao inteira: %d\n", n1 / n2);
    printf("Resto: %d\n", n1 % n2);

    return 0;
}