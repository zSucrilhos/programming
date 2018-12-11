#include <iostream>
using namespace std;

int main() {
	int x_input = 0;
	int y_input = 0;
	int remainder = 0;

	cout << "Print even numbers between X and Y" << endl;

	cout << "Type the first number: ";
	cin >> x_input;

	cout << "Type the second number: ";
	cin >> y_input;

	while (x_input < y_input) {	
		if (y_input%x_input == 0) {
			x_input = x_input + 1;
			cout << x_input << " ";
		}
	}

	return 0;
}