#include <iostream>
#include <stdlib.h>
#include <locale.h>
using namespace std;

int main (){

setlocale(LC_ALL, "Portuguese");

double valorHora, salarioBruto, salarioLiquido, ir, inss, sindicato;
int horasTrabalhadas;

cout<< ("Digite a quantidade de horas que você trabalhou esse mês: \n");
cin>> horasTrabalhadas;

cout<< ("Digite o valor que você recebe por hora: \n");
cin>> valorHora;

salarioBruto = valorHora * horasTrabalhadas;

ir = salarioBruto *0.11;

inss = salarioBruto * 0.08;

sindicato = salarioBruto * 0.05;

 salarioLiquido = salarioBruto - ir - inss - sindicato;

cout<< ("[+] Salario Bruto: ") << salarioBruto << endl;

cout<< ("[-] IR: R$") << ir << endl;

cout<< ("[-] INSS: R$") << inss << endl;

cout<< ("[-] Sindicato: R$") << sindicato << endl;

cout<< ("Total a receber: R$") << salarioLiquido << endl;


return 0;

}
