#include <iostream>
using namespace std;

int main() {
	int maior = 0;
	int menor = 0;
	int total = 0;

	cout << "Decrement between two numbers" << endl;
	cout << "Type the first number: ";
	cin >> maior;

	cout << "Type the second number: ";
	cin >> menor;

	if (maior < menor) {
		cout << "The second number is smaller, try again." << endl;
	} else if (maior == menor) {
		cout << "The numbers are the same, try again." << endl;
	} else if (maior > menor) {
		cout << "The sequence is: " << endl;
		while (maior > menor) {
			maior = maior - 1;
			cout << maior << " ";
		}	
	}

	return 0;
}