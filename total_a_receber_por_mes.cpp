#include <iostream>
#include <stdlib.h>
#include <locale.h>
using namespace std;

int main (){

setlocale(LC_ALL, "Portuguese");

float valorHora, salario;
int horasTrabalhadas;

cout<< ("Digite a quantidade de horas que você trabalhou esse mês: \n");
cin>> horasTrabalhadas;

cout<< ("Digite o valor que você recebe por hora: \n");
cin>> valorHora;

salario = valorHora * horasTrabalhadas;

cout<< ("O total que você vai receber é de ") << salario << (" reais.");

return 0;

}
