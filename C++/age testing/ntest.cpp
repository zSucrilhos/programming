#include <iostream>
using namespace std;

int main() {
	int num = 0;
	int num1 = 0;
	int num2 = 0;

	cout << "Number comparison interval" << endl;
	cout << "This program checks if the number is between a specified interval" << endl << endl;

	cout << "Type the first number: ";
	cin >> num1;
	
	cout << "Type the second number: ";
	cin >> num2;
	
	cout << "Type the number to check: ";
	cin >> num;

	if (num > num1 && num < num2) {
		cout << "The number is between the specified interval" << endl;
	} else {
		cout << "The number is outside the specified interval" << endl;
		}

	return 0;
}