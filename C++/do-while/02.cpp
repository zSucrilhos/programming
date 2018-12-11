#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double n = 0.0;
    double total = 0.0;
    cout << "Sum calculator" << endl;
    
    do {
        cout << "Enter a number to sum (type 0 to exit): ";
        cin >> n;
        total += n;
    } while (n > 0);
    cout << "The sum was: " << total << endl;

    return 0;

}
