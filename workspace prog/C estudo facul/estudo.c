#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    //declaração de variaveis
    int num1 = 10; //variavel de tipo inteiro
    float num2 = 3.14; //variavel de tipo decimal
    char caractere = 'A'; //variaevel de tipo caractere
    char frase[100] = "Ola, Mundo!"; //variavel de tipo string
    double num3 = 3.141592653589793; //variavel de tipo double /15 digitos/ de precisão dupla
    
    int valor1, valor2, soma, sub, mult, div; //variaveis para receber os valores digitados pelo usuario

    //usos do comando prinf com diversas variaveis
    printf("Hello, World!\n");
    printf("Exibindo o valor inteiro da variavel %d\n",num1);
    printf("exibindo um valor decimal, numero real %f\n",num2);
    printf("exibindo caractere %c\n",caractere); //%c para caractere
    printf("%s\n",frase); //%s para frase/string
    printf("exibindo variavel do tipo double %f\n",num3);
    printf("valores: %d %f %c %s %f\n",num1,num2,caractere,frase,num3);

//utilizando o comando scanf para receber valores do usuario
    printf("digite um numero inteiro:");
    scanf("%d",&valor1);

    printf("digite outro valor inteiro:");
    scanf("%d",&valor2);

    //operadores aritmeticos
    soma = valor1 + valor2;
    sub = valor1 - valor2;
    mult = valor1 * valor2;
    div = valor1 / valor2;

    printf("valor da soma de %d + %d = %d\n",valor1,valor2,soma);
    printf("valor da subtração de %d -%d = %d\n", valor1,valor2,sub);
    printf("valor da multiplicacao de %d * %d = %d\n",valor1,valor2,mult);
    printf("valor da divisao de %d / %d =%d\n",valor1,valor2,div);

    system("pause");
    return 0;
}