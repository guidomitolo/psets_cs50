// exercise resolved by guido mitolo

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int number, char *input[])
{
    string plaintext;
    string key;
    int duplicate = 0; // stores each character of the key in order to search for its repetition
    int place = 0; // stores the place of each character of the plaintext
    if (number > 2 || number < 2) // discards any argument not placed in the second position of the prompt
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        if (strlen(input[1]) != 26) // discards keys longer than 26 characters
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
            for (int i = 0; i < 26; i++)
            {
                if (input[1][i] < 65 || input[1][i] > 122) // discards special characters/numbers outside those ascii numbers
                {
                    printf("Usage: ./caesar key\n");
                    return 1;
                }
                else if (input[1][i] >= 91 && input[1][i] <= 96) // discards special characters/numbers inside those ascii numbers
                {
                    printf("Usage: ./caesar key\n");
                    return 1;
                }
                else
                {
                    duplicate = input[1][i];
                    for (int j = i + 1; j < 26; j++) // a nested iteration which starts at i to look after duplicated characters in the key 
                    {
                        if (duplicate == input[1][j])
                        {
                            printf("Usage: ./caesar key\n");
                            return 1;
                        }
                    }
                }
            }
        }
        plaintext = get_string("plaintext: ");
        for (int i = 0; i < strlen(plaintext); i++)
            // the substraction makes it possible to transforme the ascii code of the character in a number in order to match it with any character of the key
        {
            if (plaintext[i] >= 97 && plaintext[i] <= 122)
            {
                place = plaintext[i] - 97;
                plaintext[i] = tolower(input[1][place]);
            }
            else if (plaintext[i] >= 65 && plaintext[i] <= 90)
            {
                place = plaintext[i] - 65;
                plaintext[i] = toupper(input[1][place]);
            }
        }
        printf("ciphertext: %s\n", plaintext);
        return 0;
    }
}
