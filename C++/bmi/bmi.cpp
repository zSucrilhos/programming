#include <iostream>
using namespace std;

int main() {
    string if_var;
    double weight{0};
    double height{0};
    double bmi{0};

    cout << "Choose an unit pair: " << endl;
    cout << "1 - Kilograms and Meters\n2 - Pouds and Inches" << endl;
    cout << ">> ";
    cin >> if_var;

    if (if_var == "1") {
        cout << "Enter your weight: ";
        cin >> weight;

        cout << "Enter yout height: ";
        cin >> height;

        bmi = weight/height*2;

        cout << "Your BMI is: " << bmi << endl;

    } else if (if_var == "2") {
        cout << "Enter your weight: ";
        cin >> weight;

        cout << "Enter yout height: ";
        cin >> height;

        bmi = weight*703/height*2;

        cout << "Your BMI is: " << bmi << endl;
    } else {
        cout << "You must choose one unit pair.\n" << endl;
        system("sleep 1");
        main();
    }

    return 0;
}
