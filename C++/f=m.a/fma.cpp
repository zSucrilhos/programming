#include <iostream>

using namespace std;

int main() {
    int f, m, a = 0;
    cout << "CÁLCULO DE FORÇA (F=MxA)\n" << endl;
    
    cout << "Digite a massa: ";
    cin >> m;

    cout << "Digite a aceleração: ";
    cin >> a;

    f = m*a;
    cout << "A força é de " << f << " newtons." << endl;

    if (f <= 100) {
        cout << "Ih, fraquinho..." << endl;
    }
    else if (f > 100) {
        cout << "Forte pra porra, hein?" << endl;
    }

    return 0;
}