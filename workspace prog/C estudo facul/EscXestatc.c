#include <stdio.h>

void teste() {
    
    int local = 0;
    static int estatica = 0; 
    local++;
    estatica++;

    printf("Local: %d | Estatica: %d\n", local, estatica);
}

int main() {
    teste(); // Local: 1 | Estatica: 1 
    teste(); // Local: 1 | Estatica: 2 
    teste(); // Local: 1 | Estatica: 3 
    return 0;
}