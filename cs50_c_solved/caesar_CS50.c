#include <stdio.h>
#include <cs50.h>

int main(int number, char *text[])
{
    string plaintext;
    int digit;
    int key = 0;
    if (number > 2 || number < 2) // discards any argument not placed in the second position of the prompt
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        int m = 0;
        while (text[1][m] != '\0')
        // reads whatever was placed as the second argument of the prompt
        {
            digit = text[1][m] - '0';
            if (digit > 10)
            // rejects entries with more than a digit (i.e. characters)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
            else
            // gets the number of the key
            {
                key = key * 10 + digit;
                m++;
            }
        }
    }
    int n = 0;
    plaintext = get_string("plaintext: ");
    while (plaintext[n] != '\0')
    {
        if (plaintext[n] >= 97 && plaintext[n] <= 122) // detects a lower case character of the planetext
        {
            plaintext[n] = 97 + ((plaintext[n] - 97) + key) % 26; // rotate the character with the key
        }
        else if (plaintext[n] >= 65 && plaintext[n] <= 90) // detects a upper case character of the planetext
        {
            plaintext[n] = 65 + ((plaintext[n] - 65) + key) % 26; // rotate the character with the key
        }
        n++;
    }
    printf("ciphertext: %s\n", plaintext);
    return 0;
}