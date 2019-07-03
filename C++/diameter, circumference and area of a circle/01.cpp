#include <iostream>
using namespace std;

int main() {
	double radius = 0;
	double pi = 3.14159;
	cout << "Enter the radius of the circle: ";
	cin >> radius;

	cout << "The Diameter is: " << radius*2 << endl;
	cout << "The Area is: " << pi * radius*radius << endl;
	cout << "The Circumference is: " << 2 * pi * radius << endl;

	return 0;
}