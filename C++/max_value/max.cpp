#include <iostream>
using namespace std;

int main() {
	int arr[] = {45, 677, 89};
	int temp = 0;

	for (int n = 0; n < 3; n++) {
		if (arr[n] > temp){
			temp = arr[n];
		}
	}
	cout << "Biggest number is: " << temp << endl;

	return 0;
}