#include <stdio.h>

int main() {
    int a, b, temp;

    printf("Digite o valor de a: ");
    scanf("%d", &a);

    printf("Digite o valor de b: ");
    scanf("%d", &b);

    // Troca dos valores
    temp = a;
    a = b;
    b = temp;

    printf("\nValores após a troca:\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}