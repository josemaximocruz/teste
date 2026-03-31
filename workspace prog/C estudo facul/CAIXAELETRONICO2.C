#include <stdio.h>
#include <stdlib.h>

int  main()
{
    //declarar variaveis
    int valor = 0, n100 = 0, n50 = 0, n10 = 0, n5 = 0, n2 = 0, n1 = 0, resto = 0;
    char opcao = ' ';
    char num[100 + 1] =" ";

    do
    {
        system("cls");
        printf("****CAIXA ELETRONICO****\n");
        printf("Digite o valor do saque.\n");
        fgets(num, 100 + 1, stdin);
        valor = atoi(num);
        if (valor >= 0)
        {
            n100 = valor / 100;
            resto = valor - (n100 * 100);

             n50 = resto / 50;
            resto = resto - (n50 * 50);

            n10 = resto / 10;
            resto = resto - (n10 * 10);
            
            n5 = resto / 5;
            resto = resto - (n5 * 5);
            
             n2 = resto / 2;
            resto = resto - (n2 * 2);
            
            n1 = resto / 1;
            resto = resto - (n1 * 1);

        }
        else
        {
            main();
        }

        prinf("notas de R$100,00: %d \n", n100);
    
        prinf("notas de R$50,00: %d \n", n50);
        
        prinf("notas de R$10,00: %d \n", n10);
        
        prinf("notas de R$5,00: %d \n", n5);

        prinf("notas de R$2,00: %d \n", n2);
        
        prinf("notas de R$1,00: %d \n", n1);

        prinf("Deseja realizar outro saque? (S/N) \n");
        opcao = getch();

    } while (opcao == 'S' || opcao == 's');
    return 0;
    
}