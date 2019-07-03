// A simple program to find the first 100 prime numbers!
#include <iostream>
using namespace std;

int main() {
    for (int nmbr{1}; nmbr < 100; nmbr++) {
        while (nmbr < 100) {
            if (nmbr/nmbr == 1 and nmbr/1 == 1) {
                cout << nmbr << " is a prime number!" << endl;
            } else {
                cout << nmbr << " is not a prime number!" << endl;
            }
        }
    }
    
	
	return 0;
}
