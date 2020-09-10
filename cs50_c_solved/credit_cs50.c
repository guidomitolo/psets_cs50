#include <stdio.h>
#include <cs50.h>

int main()
{
    long i, d, v, x, y, z, two, addOne, addTwo, total;
    addOne = 0;
    addTwo = 0;
    total = 0;
    x = 1;
    y = 0;
    
    do
    {
        i = get_long("Number: ");
    }
    while (i < 0);
    
    v = ((i / 10) % 10) * 2; // divido x 10 y aplico modulo para obtener la anteultima cifra;  multiplico x 2 
    if (v >= 10) // separar las cifras/los digitos si el resultado de la multiplicación tiene dos numeros
    {
        z = v / 10 + v % 10;
    }
    else
    {
        z = v;
    }

    for (d = 0; d < 7; d++) // debo iterar el total de veces que muevo la coma (se mueve cada dos -*100-)
    {
        x = x * 100;
        y = (i / 10) / x; // corrida la coma, aplico el modulo para quedarme con la cifra
        two = (y % 10) * 2; // la multiplico por dos
        if (two >= 10) // separar las cifras/los digitos si el resultado de la multiplicación tiene dos numeros
        {
            addOne = addOne + two / 10;
            addOne = addOne + two % 10;
        }
        else
        {
            addOne = addOne + two;
        }
    }
    x = 1;
    for (d = 0; d < 7; d++)
    {
        x = x * 100;
        y = i / x;
        addTwo = addTwo + (y % 10);
    }
    // distingue la cantidad de cifras/digitos que tiene el nro. de tarjeta a fin de dividir y quedarse con la(s) primera(s) (dos) cifra(s)
    if (i > 1000000000000000) //16 visa or mastercard
    {
        y = i / 100000000000000;
    }
    else if (i > 100000000000000) //15 amex
    {
        y = i / 10000000000000;
    }
    else if (i > 1000000000000) //13 visa
    {
        y = i / 1000000000000;
    }

    total = (addOne + z) + (addTwo + (i % 10)); 
    // la suma de todos las cifras multiplicadas por dos (inluída al anteultima) más el restro de las cifras

    if (total % 10 == 0 && y == 34)
    {
        printf("AMEX\n");
    }
    else if (total % 10 == 0 && y == 37)
    {
        printf("AMEX\n");
    }
    else if (total % 10 == 0 && 50 < y && y < 56)
    {
        printf("MASTERCARD\n");
    }
    else if (total % 10 == 0 && y / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}

/*
4012888888881881
American Express uses 15-digit numbers,  start with 34 or 37
MasterCard uses 16-digit numbers, tart with 51, 52,53, 54, or 55
Visa uses 13- and 16-digit numbers, start with 4 (davids = 16)
*/
