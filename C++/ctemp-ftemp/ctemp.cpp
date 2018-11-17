#include <iostream>
using namespace std;

int main() {
    
    double ctemp = 0.0;
    double ftemp = 0.0;

    cout << "CONVERSOR DE FAHRENHEIT PARA CELSIUS" << endl;
    cout << "Digite a temperatura em Fahrenheit para a conversão: ";
    cin >> ftemp;
    ctemp = (ftemp - 32) / 1.8;
    cout << "A temperatura convertida para celsius é de: " << ctemp << "º" << endl;

    return 0;
}

