//Fazer programa que lê 2 números e imprima "eles são pares" se forem

#include <stdio.h>
int main() {

    int num1, num2;
    printf("DIgite o primeiro numero;");
    scanf("%d", &num1);

    printf("Digite o segundo numero:");
    scanf("%d", &num2);

    if(num1 % 2 == 0 && num2 % 2 == 0) {
        printf("ambos sao pares\n");
    } 
    else {
        printf("os 2 numeros nao sao pares\n");
    } 
    
    if((num1 % 2 == 0) ^ (num2 % 2 == 0)) {
        printf("apenas um dos numeros eh par\n");
    } 
    
    if(num1 % 2 == 0 ) {
        printf("o numero %d eh par\n", num1);
    } 
    
    else if (num1 % 2 != 0 ) {
        printf("o numero %d eh impar\n", num1);
    } 
    
    if(num2 % 2 == 0) {
        printf("o numero %d eh par\n", num2);
    } else if (num2 % 2 != 0 ) {
        printf("o numero %d é impar\n", num2);
    } 

    return 0;
}