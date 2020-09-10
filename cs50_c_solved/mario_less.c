#include <cs50.h>
#include <stdio.h>

int positivo_int (string prompt);

int main(void)

{
    int z;
    z = positivo_int ("Dame un nro.: \n");

    for (int i = 0; i < z; i++)
    {
        for (int k = 8; k > i; k--)
        {
            printf (" ");
        }   
        for (int j = -1; j < i; j++)
        {
            printf ("#");
        }
        
        printf ("\n");
    }
}

int positivo_int (string prompt)
    
{
    int x;
    do
    {
        x = get_int ("%s", prompt);        
    }
    while (x < 0 || x > 8);
    return x;
}
