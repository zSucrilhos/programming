// Find the first 100 prime numbers
#include <iostream>
using namespace std;

int main() {
	cout << "100 first prime number calculator" << endl;
	for (int i = 0; i < 100; i++) {
		if (i / i == 1 and i / 1 == i) {
			cout << i << " is a prime number!" << endl;
		} else {
			cout << i << " is not a prime number" << endl;
		}
	}

	return 0;
}
