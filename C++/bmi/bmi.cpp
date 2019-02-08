#include <iostream>
using namespace std;

int main() {
	char unit = 's';
	double bmi = 0;
	double weightx2 = 0;
	double poundsx703 = 0;
	double height = 0;
	double weight = 0;

	cout << "Body-mass Index calculator\n" << endl;

	cout << "Select the units for the measurements:\n\
	'M' to Meters and Kilograms\n\
	'P' to Inches and Pounds" << endl;
	cin >> unit;

	cout << "According to the Department of Health and Human Services/National Institutes of Health\n" << endl;
	cout << "BMI VALUES\n\
Underweight: less than 18.5\n\
Normal:      between 18.5 and 24.9\n\
Overweight:  between 25 and 29.9\n" << endl;

	if (unit == "M") {		
		cout << "Enter your height in Meters: ";
		cin >> height;

		cout << "Enter your weight in Kilograms: ";
		cin >> weight;
		weightx2 = weight*2;
		bmi = weight/weightx2;

		cout << "Your BMI is: " << bmi;
	} else if (unit == "P") {
		cout << "Enter your height in Inches: ";
		cin >> height;

		cout << "Enter your weight in Pounds: ";
		cin >> weight;

		poundsx703 = weight * 703;
		weightx2 = weight*2;
		bmi = poundsx703/weightx2;

		cout << "Your BMI is: " << bmi;
	} else {
		cout << "WROONG WAY" << endl;
	}
	
	return 0;
}