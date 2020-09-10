#include <stdio.h>
int main (void) {
double fpago;
scanf ("%lf", &fpago);
int pago = fpago*100;
int veinticinco = pago/25;
int restoUno= pago%25;
int diez = restoUno/10;
int restoDos = restoUno%10;
int cinco = restoDos/5;
int restoTres = restoDos%5;
int total = veinticinco + diez + cinco + restoTres;
printf("%d\n", total);
return 0;}