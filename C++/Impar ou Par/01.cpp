#include <iostream>
using namespace std;

int main() {

	int resto = 0;
	int numero = 0;

	cout << "Impar ou par\n";

	cout << "Digite o numero desejado: ";
	cin >> numero;

	resto = numero % 2;

	if (resto == 0) {
		cout << "O numero e par!" << endl;
	} else {
		cout << "O numero e impar!" << endl;
	}


	return 0;
}