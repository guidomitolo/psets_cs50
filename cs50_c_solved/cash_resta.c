# include <stdio.h>
# include <math.h>
# include <cs50.h>
  
int main (void) {
    float vuelto;
    do{
        vuelto = get_float ("");
    }
    while (vuelto < 0);
    int centavos = round (vuelto * 100);
    int monedas = 0;
    while (centavos >= 25){
        (centavos = centavos - 25);
        monedas ++;    
    }
    while  (centavos < 25 && centavos >= 10){
        (centavos = centavos - 10);
        (monedas ++);
    }
    while  (centavos < 10 && centavos >= 5){
        (centavos = centavos - 5);
        (monedas ++);
    }
    while (centavos < 5 && centavos >= 1){
        (centavos = centavos - 1);
        (monedas ++);
    }
    printf ("%i\n", monedas);
    return 0;
}
