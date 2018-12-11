#include <iostream>
using namespace std;

int main() {
	int n = 0;
	n--;
	cout << n << endl;
	
	if (n--) {
		cout << n;
	}

	return 0;
}