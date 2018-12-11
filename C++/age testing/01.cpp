#include <iostream>
using namespace std;

int main() {
	int age = 0;

	cout << "what is your age? ";
	cin >> age;
	
	if(age < 2) {
		cout << "youre a baby!" << endl;
	} else if (age > 2 && age < 13) {
		cout << "youre a children!" << endl;
	} else if (age > 13 && age < 20) {
		cout << "youre a teenager!" << endl;
	} else if (age > 20 && age < 60) {
		cout << "youre a adult!" << endl;
	} else if (age > 60 && age < 100) {
		cout << "youre a old person!" << endl;
	} else if (age > 100) {
		cout << "youre DEAD!" << endl;
	}		


	return 0;

}
