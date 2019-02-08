// Print all the square numbers to 100

#include <iostream>
using namespace std;

int main() {
	for (int a = 1; a < 100; a++) {
		//cout << a;
		int square_nmbr = a*a;
		cout << " The square of the number " << a << " is: " << square_nmbr << endl;
	}

	return 0;
}
