//Ler 3 números e imprimir em ordem crescente

#include <stdio.h>
int main()
{

    int num1, num2, num3;

    printf("digite um numero inteiro: ");
    scanf("%d", &num1);

    printf("digite outro numero inteiro: ");
    scanf("%d", &num2);

    printf("digite o ultimo numero inteiro: ");
    scanf("%d", &num3);

    if (num1 > num2 && num1 > num3 && num2 > num3)
    {
        printf("o maior eh %d, o do meio eh o %d e o menor eh o %d\n", num1, num2, num3);
    }
    else  if (num1 > num2 && num1 > num3 && num2 < num3)
    {
        printf("o maior eh %d, o do meio eh o %d e o menor eh o %d\n", num1, num3, num2);
    }
    else if (num2 > num1 && num2 > num3 && num1 > num3)
    {
        printf("o maior eh o %d, o do meio eh o %d e o menor eh o %d\n", num2, num1, num3);
    }
    else if (num2 > num1 && num2 > num3 && num1 < num3)
    {
        printf("o maior eh o %d, o do meio eh o %d e o menor eh o %d\n", num2, num3, num1);
    }
    else if(num3 > num1 && num3 > num2 && num1 > num2)
    {
        printf("o maior eh o %d, o do meio eh o %d e o menor eh o %d\n", num3, num1, num2);
    }
        else if(num3 > num1 && num3 > num2 && num1 < num2)
    {
        printf("o maior eh o %d, o do meio eh o %d e o menor eh o %d\n", num3, num2, num1);
    }
     else if( num1 == num2 && num2 == num3)
    {
        printf("os numeros sao iguais\n");
    }

    return 0;
}