#include <iostream>

using namespace std;

int main() {
    int idade = 0;
    cout << "Qual a sua idade? ";
    cin >> idade;

    if (idade == 18) {
        cout << "Rapaz, você tem " << idade << " anos!" << endl;
        cout << "Legal! \nHAHA" << endl;
    }
    else {
        cout << "Então a sua idade é " << idade << endl;
        cout << "Muito bem!" << endl;
    }


    return 0;
}

