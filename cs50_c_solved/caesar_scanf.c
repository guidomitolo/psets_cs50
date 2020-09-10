#include <stdio.h>

int main (int number, char * text[]) {
    
    char plaintext[20];
    int digit;
    int key = 0;
    if (number > 2){
        printf("Usage: ./caesar key\n");
        return 1;
    }else{
        int m = 0;
        while (text[1][m] != '\0'){
            digit = text[1][m] - '0';
            if (digit > 10){  // rechazar entradas (digit) que contengan más de un digito por vez
                printf("Usage: ./caesar key\n");
                return 1;
            }else{
                key = key * 10 + digit;
                m++;
            }
        }
    }
    int n = 0;
    printf("plaintext: ");
    scanf("%s", plaintext);
    while (plaintext[n] != '\0'){ // recorrer el array plaintext
        if (plaintext [n] == 122 || plaintext [n] == 90){
            plaintext [n] = plaintext [n] - 25; // transformar z/Z en a/A
            plaintext [n] = plaintext [n] + (key-1); // rotar "digit" veces -1 (excluyendo a/A)
            n++;
        }else{
            plaintext[n] = plaintext[n]+key;
            n++;
        }
    }   
    printf("ciphertext: %s\n", plaintext);
    return 0;
}