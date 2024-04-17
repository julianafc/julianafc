#include <iostream>
#include <stdlib.h>
#include <locale.h>
using namespace std;

float n1, n2, n3, n4, media;

int main (){

setlocale(LC_ALL, "Portuguese");

string nome;

cout<< ("Digite o seu nome: \n");
getline(cin, nome);
cout<< ("Digite a primeira nota: \n");
cin>> n1;
cout<< ("Digite a segunda nota: \n");
cin>> n2;
cout<< ("Digite a terceira nota: \n");
cin>> n3;
cout<< ("Digite a quarta nota: \n");
cin>> n4;

media = (n1 + n2 + n3 + n4) / 4;

cout<< ("As notas do aluno ") << nome << (" são: ") << n1 << (", ") << n2 << (", ") << n3 << (" e ") << n4 << (" e a média é de: ") << media;

return 0;
}
