#include <iostream>
using namespace std;

int main() {
	int numA = 0;
	int numB = 0;

	cout << "Type two numbers: ";
	cin >> numA >> numB;

	if (numA % numB == 0) {
		cout << "The two are multiples from another" << endl;
	} else {
		cout << "They aren't multiples from the another" << endl;
	}

	return 0;
}