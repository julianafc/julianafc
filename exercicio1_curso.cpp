#include <iostream>
#include <stdlib.h>
#include <locale.h>
using namespace std;

int main (){

setlocale(LC_ALL, "Portuguese");

float metros, centimetros;

cout<< ("Digite a quantidade de metros que você quer converter:\n");
cin>> metros;

centimetros = metros * 100;

cout<< ("---------------------------------------------- \n");
cout<< centimetros;

return 0;
}
