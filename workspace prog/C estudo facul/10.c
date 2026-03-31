#include <stdio.h>

int main() {

   int a = 10, b = 5, c = 10; 

printf("%d\n", a > b && b < c); 

printf("%d\n", a == c || b > a); 

printf("%d\n", !(a == b)); 

printf("%d\n", a != c && b <= c); 

 

    return 0;
}