//Ler 2 num e printar o maior

#include <stdio.h>
int main()
{

    int num1, num2;

    printf("digite um numero inteiro: ");
    scanf("%d", &num1);

    printf("digite outro numero inteiro: ");
    scanf("%d", &num2);

    if (num1 > num2)
    {
        printf(" %d eh maior que %d \n", num1,  num2);
    } else if (num2 > num1)
    {
        printf(" %d eh maior que %d \n", num2, num1);
    } else
    { 
        printf("os 2 numeros sao iguais");
    }

    return 0;
}