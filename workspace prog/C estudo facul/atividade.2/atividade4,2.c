/*4)
Indentificar e organizar pessoas em times de um campeonator idado pe 

1-10 t = infantil 
11-18 t = infantil plus
19-25 t = quase gente 
26-35 t = já paga boleto
36-50 t = adulto
51+ t = adulto plus*/

#include <stdio.h>
int main()
{

    int idade;
    printf("digite sua idade: ");
    scanf("%d", &idade);

    if(idade >= 1 && idade <=10)
    {
        printf("voce esta no time infantil\n");
    }
    else if (idade >= 11 && idade <= 18)
    {
        printf("voce esta no time dos infantil plus\n");
    }
    else if(idade >= 19 && idade <=25)
    {
        printf("voce esta no time dos quase gente\n");
    }
    else if(idade >= 26 && idade<= 35)
    {
        printf("voce esta no time que ja paga boleto\n");
    }
    else if (idade >= 36 && idade <= 50)
    {
        printf("voce esta no time dos adulto\n");
    }    
    else if(idade >= 51)
    {
        printf("voce esta no time de matusalem\n");
    }

    return 0;
}