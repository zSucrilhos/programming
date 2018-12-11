#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int n = 0;
    cout << "Type a number and the system will tell it to you: ";
    cin >> n;

    switch(n) {
        case 1:
                cout << "number one" << endl;
                break;
        case 2:
                cout << "number two" << endl;
        case 3:
                cout << "number three" << endl;
                break;
        case 4:
                cout << "number four" << endl;
                break;
        case 5:
                cout << "number five" << endl;
                break;
    }
    
    cout << "My name is erick, and this is only a test" << endl;

    return 0;
}
