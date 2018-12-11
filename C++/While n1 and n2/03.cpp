#include <iostream>
using namespace std;

int main() {
	int n1 = 0;
	int n2 = 0;
	int total = 0;

	cout << "Increment between two numbers" << endl;
	cout << "Type the first number: ";
	cin >> n1;

	cout << "Type the second number: ";
	cin >> n2;

	if (n2 < n1) {
		cout << "The second number is small than the first, try again.";
	} else if (n2 == n1) {
		cout << "The numbers are the same, try again.";
	} else if (n2 > n1) {
		cout << "The sequence is: " << endl;
		while (n1 < n2) {
			n1 = n1 + 1;
			cout << n1 << " ";
		}
	}

	return 0;
}