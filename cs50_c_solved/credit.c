# include <stdio.h>
int main (){
    long i,d,x,y,z,two,addOne,addTwo, total;
    addOne = 0;
    addTwo = 0;
    total = 0;
    x = 1;
    y = 0;
    printf ("Number: ");
    scanf("%ld", &i);
    z = ((i/10)%10)*2; // divido x 10 y aplico modulo para obtener la anteultima cifra;  multiplico x 2
    for (d = 0; d < 7; d++){ // debo iterar el total de veces que muevo la coma (se mueve cada dos -*100-)
        x = x*100;
        y = (i/10)/x; // corrida la coma, aplico el modulo para quedarme con la cifra
        two = (y%10)*2; // la multiplico por dos
        if (two>=10){ // separar las cifras si el resultado de la multiplicación tiene dos numeros
            addOne = addOne + two/10;
            addOne = addOne + two%10;
        }
        else
            addOne = addOne + two;            
    }
    x = 1;
    for (d = 0; d < 7; d++){
        x = x*100;
        y = i/x;
        addTwo = addTwo + (y%10);
    }
    // distinguir cuantas cifras tiene el nro. de tarjeta para dividir y quedarse con la(s) ultima(s) (dos) cifra(s)
    if (i>1000000000000000)
        y = i/10000000000000;
    else if (i>100000000000000)
        y = i/10000000000000;
    else if (i>1000000000000)
        y = i/1000000000000;
    total =  (addOne+z)+(addTwo+(i%10)); // la suma de todos las cifras multiplicadas por dos (inluída al anteultima) más el restro de las cifras
    if (total%10 == 0 && y == 34)
        printf("AMEX\n");
    else if (total%10 == 0 && y == 37)
        printf("AMEX\n");
    else if (total%10 == 0 && 50 < y && y < 56)
        printf("MASTERCARD\n");
    else if (total%10 == 0 && y == 4)
        printf("VISA\n");
    else
        printf("INVALID\n");
    return 0;
}