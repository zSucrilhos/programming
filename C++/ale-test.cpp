#include <iostream>
#include <iostream>
using namespace std;

int main(){
    string a = "";
    cout << "Digite o seu nome" << endl;
    cin >> a;

    if(a=="Erick"){
        cout << "Olá Erick :)" << endl;
    } else{
        cout << "Olá " << a << endl;
    }

    return 0;
}

