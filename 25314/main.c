#include <stdio.h>

int main() {
    int n = 0;
    scanf("%d", &n);

    int iter = n / 4;

    for (int i = 0; i < iter; i++) {
        printf("long ");
    }
    printf("int");
}