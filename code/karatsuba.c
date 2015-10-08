#include <stdio.h>
#include <math.h>

int karatsuba();
int size_int();
int * get_half();

int main(){
  int a, b, c, d, up, down;
  int *number;
  printf("Favor de ingresar el primer numero a ser multiplicado: ");
  scanf("%d",&a);
  printf("Favor de ingresar el segundo numero a ser multiplicado: ");
  scanf("%d",&b);
  c = a * b;
  printf("El resultado es: %d \n", c);
  d = size_int(c);
  number = up_low(c);
  printf("La mitad superior de %d es: %d \n",c, number[0]);

  printf("La mitad inferiro de %d es: %d \n",c, number[1]);

  return 0;
}

int size_int(int n){
  int size_int;
  size_int =  floor(log10(abs(n))) + 1;
  return size_int;
}

int *  get_half(int n){
  int size, half;
  int up_low[2];
  size = size_int(n);
  if(size % 2 == 0){
    half = pow(10, size/2);
    up_low[0] = floor(n/half);
    up_low[1] = n - up_low[0]*half;
  }
  return up_low;
}
