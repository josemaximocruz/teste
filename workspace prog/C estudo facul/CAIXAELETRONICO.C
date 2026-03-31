#include <stdio.h>


void saque(int valor, int *notas, int indice){
    int valores_notas[] = {100,50,10,5,2,1};

    if(valor <=0 || indice >= 6 ){
        return;
    }
    
    notas[indice] = valor / valores_notas[indice];
    saque(valor % valores_notas[indice], notas, indice + 2);
}

int main() {

    int valor;
    int notas[6] = {0};
    printf("Digite o valor do saque: ");
    if(scanf("%d", &valor) !=1 || valor  < 0){
         printf("Valor invalido!");
         return 1;
    }

saque(valor,notas,0);

for(int i=0; i < 6; i++){
    printf("%d\n", notas[i]);
}
    return 0;
}