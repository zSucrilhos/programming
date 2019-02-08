#include <iostream>
using namespace std;

int main() {
	int age{0};

	cout << "Enter your age: ";
	cin >> age;

	if (age <= 2) {
		cout << "You are a baby" << endl;
	} else if (age > 2 and age <= 12) {
		cout << "You are a kid" << endl;
	} else if (age > 12 and age <= 18) {
		cout << "You are a teenager" << endl;
	} else if (age > 18 and age <= 65) {
		cout << "You are a adult" << endl;
	} else if (age > 65 and age <= 90) {
		cout << "You are an old person" << endl;
	} else if (age > 90 and age <= 105) {
		cout << "Impressive! You lived really a long time" << endl;
	} else if (age > 105 and age <= 115) {
		cout << "Wow! You're pretty old, aren't you?!" << endl;
	} else if (age > 115) {
		cout << "HOW'S THAT EVEN POSSIBLE ?!?!" << endl;
	}

	return 0;
}
