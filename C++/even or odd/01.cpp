// Given an interval of two numbers, print only the even ones
#include <iostream>
#include <cmath>
using namespace std;

int main() {

	int num1 = 0;
	int num2 = 0;
	int c = 0;

	system("CLS");

	cout << "Given an interval of two numbers, print only the even ones" << endl << "\n";
	cout << "Enter the first number: ";
	cin >> num1;

	cout << "Enter the second number: ";
	cin >> num2;

	if (num1 > num2) {
		cout << "Please enter only the higher number first" << endl;
	} else {
		while (num1 < num2) {
			++num1;
			++c;
			if (num1%2 == 0) {
				cout << num1 << " ";
			}
		}
		cout << endl << "Total amount of numbers: ";
		c = c - 1;
		cout << c << endl;
	}
	

	return 0;
}

