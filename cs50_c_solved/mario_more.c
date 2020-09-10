# include <stdio.h>

int main (){
    int i, j, k, n;
    scanf("%d", &n);
    while (n <= 0 || n >= 9)
        scanf("%d", &n);
    for (i = 0; i<n; i++){ // nro. de renglones
        for (k = 7; k > i; k--)  // nro. decreciente de espacios (de 7 a i)
            printf(" ");            
        for (k = -1; k < i; k++) // nro. creciente de símbolos (de -1 a i)
            printf("#");            
        printf("  ");
        for (k = -1; k < i; k++)
            printf("#");            
        for (k = 7; k > i; k--)
            printf(" ");            
        printf("\n");            
    }
            printf("\n");            
}