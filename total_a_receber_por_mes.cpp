#include <iostream>
#include <stdlib.h>
#include <locale.h>
using namespace std;

int main (){

setlocale(LC_ALL, "Portuguese");

float valorHora, salario;
int horasTrabalhadas;

cout<< ("Digite a quantidade de horas que voc� trabalhou esse m�s: \n");
cin>> horasTrabalhadas;

cout<< ("Digite o valor que voc� recebe por hora: \n");
cin>> valorHora;

salario = valorHora * horasTrabalhadas;

cout<< ("O total que voc� vai receber � de ") << salario << (" reais.");

return 0;

}
